from __future__ import annotations

############################################################
# Pour permettre de lancer les tests...
#######################################
import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
############################################################
from time import sleep
import random
from CLASSES.Grille import Grille
from CLASSES.Poisson import Poisson
from CLASSES.Requin import Requin
from CLASSES.Rocher import Rocher, positions_de_la_cavite
import gestionnaire
from parametres import (
    NOMBRE_LIGNE_GRILLE,
    NOMBRE_COLONNE_GRILLE,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_REQUIN,
    TEMPS_RAFRAICHISSEMENT,
    INCLURE_REFUGE,
)
from emojis import (
    symbole_case_vide,
    symbole_poisson,
    symbole_requin,
    symbole_inconnu,
    symbole_rocher,
)

random.seed()


# Classe qui représente le monde Wa-Tor
class Monde:
    # region Méthode:__init__
    def __init__(self) -> None:
        """
        Constructeur de la classe Monde.
        Initialise la grille du monde et le chronon.
        """
        self.grille = Grille(NOMBRE_COLONNE_GRILLE, NOMBRE_LIGNE_GRILLE)
        self.chronon = 0
        self.colonnes = NOMBRE_COLONNE_GRILLE
        self.lignes = NOMBRE_LIGNE_GRILLE

    # region Méthode:initialiser
    def initialiser(
        self,
        classe_poisson: Poisson = Poisson,
        classe_requin: Requin = Requin,
        nb_poissons: int = NOMBRE_INITIAUX_POISSON,
        nb_requins: int = NOMBRE_INITIAUX_REQUIN,
    ) -> None:
        """
        Initialise le monde avec un nombre donné de poissons et de requins.
        Les entités sont placées aléatoirement sur la grille.

        Args:
            nb_poissons (int): Nombre de poissons à placer.
            nb_requins (int): Nombre de requins à placer.
            classe_poisson (Poisson): Classe du poisson.
            classe_requin (Requin): Classe du requin.

        Returns:
            None
        """
        # Vérification des paramètres d'entrée
        if nb_poissons < 0:
            raise ValueError("Le nombre de poissons initial doit être positif.")
        if nb_requins < 0:
            raise ValueError("Le nombre de requins initial doit être positif.")
        self.est_suffisamment_grand(nb_poissons + nb_requins)

        # Liste de toutes les positions de la grille
        toutes_les_positions = self.toutes_les_positions()

        # Placement du refuge
        if INCLURE_REFUGE:
            self.placer_les_rochers(
                positions_de_la_cavite((0, 0)), toutes_les_positions
            )

        # Liste aléatoire de toutes les positions restantes
        random.shuffle(toutes_les_positions)

        # Placement des espèces dans la grille
        self.placer_une_espece(classe_poisson, nb_poissons, toutes_les_positions)
        self.placer_une_espece(classe_requin, nb_requins, toutes_les_positions)

    # region Méthode:est_suffisamment_grand
    def est_suffisamment_grand(self, nb_entites: int) -> None:
        """Vérifie si la taille de la grille est suffisament grand par
        rapport au nombre de poissons et nombres de requins demandés
        initialement.

        Args:
            nb_entites (int): Nombre d'entités.

        Raises:
            ValueError: Si le nombre d'entités est plus grand que le nombre de case,
            lève l'erreur.
        """
        if self.lignes * self.colonnes < nb_entites:
            raise ValueError(
                f"Le nombre initial de poissons et de requins ({nb_entites}) est trop grand pour la taille de grille\nTaille de la grille: {self.lignes}X{self.colonnes}"
            )

    # region Méthode:placement_entites
    def placer_une_espece(
        self,
        classe_espece: Poisson | Requin,
        nb_entites: int,
        positions_possibles: list[tuple[int, int]],
    ) -> None:
        """Placer un nombre prédéfini d'entités dans la grille pour une certaine espèce.

        Args:
            classe_espece (Poisson | Requin): Espèce concernée
            nb_entites (int): Nombre d'entités à placer
            positions_possibles (list[tuple[int, int]]): Liste des positions encore disponibles dans la grille.
        """
        for _ in range(nb_entites):
            if not positions_possibles:
                break
            (x, y) = positions_possibles.pop()
            entite = classe_espece((x, y))
            self.grille.placer_entite((x, y), entite)

    # region Méthode:placement_rochers
    def placer_les_rochers(
        self,
        positions_souhaitées: list[tuple[int, int]],
        positions_possibles: list[tuple[int, int]],
    ) -> None:
        """Placer un nombre prédéfini de rochers aux positions souhaitées en vérifiant que ces positions sont possibles.

        Args:
            positions_souhaitées (list[tuple[int, int]]): Liste des positions souhaitées pour les rochers dans la grille.
            positions_possibles (list[tuple[int, int]]): Liste des positions encore disponibles dans la grille.
        """
        for position in positions_souhaitées:
            if positions_possibles.count(position) == 0:
                continue
            else:
                # Ajout d'un rocher
                self.grille.placer_entite(position, Rocher())

                # Enlever la position des positions possibles
                positions_possibles.pop(positions_possibles.index(position))

    # region Méthode:toute_positions
    def toutes_les_positions(self) -> list[tuple[int, int]]:
        """
        Renvoie une liste de toutes les positions de la grille.

        Returns:
            list[tuple[int, int]]: Liste des positions (x, y) de la grille.
        """
        return [(x, y) for x in range(self.colonnes) for y in range(self.lignes)]

    # region Méthode:executer_chronon
    def executer_chronon(self) -> None:
        """
        Exécute un chronon du monde Wa-Tor.
        Chaque entité vieillit, se déplace et se reproduit si nécessaire.
        Les entités sont traitées dans un ordre aléatoire pour simuler le comportement du monde.

        Returns:
            None
        """
        # Incrément du chronon
        self.chronon += 1

        # Obtenir une liste aléatoires de toutes les positions dans la grille
        toutes_les_positions = self.toutes_les_positions()

        # Parcourir les entités et éxecuter les effets du temps
        for x, y in toutes_les_positions:
            entite = self.grille.lire_case((x, y))
            if entite == None or isinstance(entite, Rocher):
                continue

            # Effet du temps qui passe
            entite.vieillir()
            entite.mourir()

            # Nettoyage. Note:
            # cela empechera les requins de manger des poissons morts
            # cela permettra aux autres entites de se déplacer sur les case occupées par les entités mortes
            self.grille.nettoyer_case((x, y))

        self.executer_toutes_les_actions()

        # Parcourir les entités pour nettoyer les morts
        for x, y in toutes_les_positions:
            entite = self.grille.lire_case((x, y))
            if entite == None or isinstance(entite, Rocher):
                continue

            # Nettoyage
            self.grille.nettoyer_case((x, y))

    # region Méthode: executer_toutes_les_actions
    def executer_toutes_les_actions(self) -> None:
        """
        Exécute toutes les actions des entités dans le monde.
        Les requins agissent en premier, suivis des poissons.

        Returns:
            None
        """
        # Liste aléatoires de toutes les positions de la grille
        toutes_les_positions = self.toutes_les_positions()
        random.shuffle(toutes_les_positions)

        # liste des positions des entités qui ont déjà agi
        deja_agis = []

        # Execution des actions, une espèce après l'autre
        self.executer_toutes_les_actions_des_requins(toutes_les_positions, deja_agis)
        self.executer_toutes_les_actions_des_poissons(toutes_les_positions, deja_agis)

    # region Méthode: executer_toutes_les_actions_des_requins
    def executer_toutes_les_actions_des_requins(
        self, toutes_les_positions: list[tuple[int, int]], deja_agis: list
    ) -> None:
        """Exécute toutes les actions des requins dans le monde.
        Chaque requin peut se reproduire, manger ou se déplacer, en fonction des possibilités offertes par les case voisines.
        Les requins agissent dans un ordre aléatoire pour simuler le comportement du monde.

        Args:
            toutes_les_positions (list[tuple[int,int]]): Toutes les positions qui n'ont pas encore été inspectées pour action à ce chronon.
            deja_agis (list): Liste des positions des entités qui ont déjà agis durant ce chronon.
        """

        for position in toutes_les_positions:
            entite = self.grille.lire_case(position)

            if all([isinstance(entite, Requin), not position in deja_agis]):
                # Liste des positions des cases voisines (total et selon type)
                positions_voisines = self.grille.cases_voisines(position)
                positions_voisines_vides = self.grille.cases_voisines_libres(
                    position, positions_voisines
                )
                positions_voisines_poissons = self.grille.cases_voisines_entites(
                    Poisson, position, positions_voisines
                )
                positions_voisines_requins_adultes = self.grille.cases_voisines_entites(
                    Requin, position, positions_voisines, filtre_adulte=True
                )

                # S'il y a au moins une case vide autour:
                if len(positions_voisines_vides) > 0:
                    # Un requin se reproduit en priorité
                    if gestionnaire.execute_se_reproduire_entite(
                        entite,
                        position,
                        positions_voisines_vides,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon, s’il a faim mais pas trop et qu'un autre requin est proche, il defend son territoire
                    elif gestionnaire.execute_combattre_requin(
                        entite,
                        position,
                        positions_voisines_requins_adultes,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon, s’il peut manger un poisson et s'il a faim, il le fait
                    elif gestionnaire.execute_s_alimenter_requin(
                        entite,
                        position,
                        positions_voisines_poissons,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon, il se déplace aléatoirement
                    elif gestionnaire.execute_se_deplacer_entite(
                        entite,
                        position,
                        positions_voisines_vides,
                        self.grille,
                        deja_agis,
                    ):
                        continue

                # S'il n'y a aucune case vide autour:
                else:
                    # Si un requin a faim mais pas trop et qu'un autre requin est proche, il defend son territoire
                    if gestionnaire.execute_combattre_requin(
                        entite,
                        position,
                        positions_voisines_requins_adultes,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon, s'il peut manger un poisson et s'il a faim, il le fait
                    elif gestionnaire.execute_s_alimenter_requin(
                        entite,
                        position,
                        positions_voisines_poissons,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon il ne bouge pas (bloqué)

    # region Méthode: executer_toutes_les_actions_des_poissons
    def executer_toutes_les_actions_des_poissons(
        self, toutes_les_positions: list[tuple[int, int]], deja_agis: list
    ) -> None:
        """Exécute toutes les actions des poissons dans le monde.
        Chaque poisson peut se reproduire, manger ou se déplacer, en fonction des possibilités offertes par les case voisines.
        Les poissons agissent dans un ordre aléatoire pour simuler le comportement du monde.

        Args:
            toutes_les_positions (list[tuple[int,int]]): Toutes les positions qui n'ont pas encore été inspectées pour action à ce chronon.
            deja_agis (list): Liste des positions des entités qui ont déjà agis durant ce chronon.
        """

        for position in toutes_les_positions:
            entite = self.grille.lire_case(position)

            if all([isinstance(entite, Poisson), not position in deja_agis]):
                # Liste des positions des cases voisines (selon type)
                positions_voisines_vides = self.grille.cases_voisines_libres(position)

                # S'il y a au moins une case vide autour:
                if len(positions_voisines_vides) > 0:
                    # Un poisson se reproduit en priorité
                    if gestionnaire.execute_se_reproduire_entite(
                        entite,
                        position,
                        positions_voisines_vides,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                    # Sinon, il se déplace aléatoirement
                    elif gestionnaire.execute_se_deplacer_entite(
                        entite,
                        position,
                        positions_voisines_vides,
                        self.grille,
                        deja_agis,
                    ):
                        continue
                # Sinon il ne bouge pas (bloqué)

    # region Méthode: afficher
    def afficher(self, param_sleep: bool = True) -> None:
        """
        Affiche la grille du monde avec les entités présentes.
        Chaque case est représentée par un emoji correspondant à l'entité présente.
        Les cases vides sont représentées par un emoji d'eau.
        Les poissons et requins sont représentés par leurs emojis respectifs.
        Si param_sleep est True, la fonction attend un certain temps avant de rafraîchir l'affichage.

        Returns:
            None: Affiche la grille dans le terminal.
        """
        for y in range(self.lignes):
            ligne_separateur = "+"
            ligne = "|"
            for x in range(self.colonnes):
                entite = self.grille.lire_case((x, y))
                if entite is None:
                    ligne += symbole_case_vide()
                elif isinstance(entite, Poisson):
                    ligne += symbole_poisson()
                elif isinstance(entite, Requin):
                    ligne += symbole_requin()
                elif isinstance(entite, Rocher):
                    ligne += symbole_rocher()
                else:
                    ligne += symbole_inconnu()
                ligne_separateur += "--+"
                ligne += "|"

            if y == 0:
                print("+--------------+")
                print("| WA-TOR WORLD |")
                print("+--------------+\n")
                print(f"Chronon: {self.chronon}\n")
                print(f" Nombre poisson: {self.grille.nombre_espece(Poisson)}")
                print(f" Nombre requin: {self.grille.nombre_espece(Requin)}")

            print(ligne_separateur)
            print(ligne)
        else:
            print(ligne_separateur)

        if param_sleep:
            sleep(TEMPS_RAFRAICHISSEMENT)

    # region Méthode __repr__
    def __repr__(self) -> str:
        """
        Affichage terminal
        """
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"


# region TEST
def test():
    # Test de grille ici pour éviter les dependances circulaires
    grille_demo = Grille(5, 1)
    print("Cases voisines (monde 1D)")
    print(grille_demo.cases_voisines((2, 0)))

    grille_demo = Grille(5, 3)
    print("Cases voisines (monde 2D)")
    print(grille_demo.cases_voisines((2, 0)))

    grille_demo = Grille(5, 5)
    grille_demo.placer_entite((2, 3), Poisson((2, 3)))
    grille_demo.placer_entite((4, 3), Poisson((4, 3)))
    print("Cases voisines vides (monde 2D)")
    print(grille_demo.cases_voisines_libres((3, 3)))

    grille_demo.placer_entite((3, 2), Requin((3, 2)))
    requin = Requin((3, 4))
    requin._est_bebe = False
    grille_demo.placer_entite((3, 4), requin)
    print("Cases voisines poissons (monde 2D)")
    print(grille_demo.cases_voisines_entites(Poisson, (3, 3)))
    print("Cases voisines requins (monde 2D)")
    print(grille_demo.cases_voisines_entites(Requin, (3, 3)))
    print("Cases voisines requins (monde 2D)")
    print(grille_demo.cases_voisines_entites(Requin, (3, 3), filtre_adulte=True))

    # Test placer_des_rochers
    monde = Monde()
    toutes_les_positions = monde.toutes_les_positions()
    monde.placer_les_rochers(positions_de_la_cavite((0, 0)), toutes_les_positions)
    monde.afficher()
    print(toutes_les_positions)

    # Création du monde et initialisation
    monde = Monde()
    monde.initialiser(
        classe_poisson=Poisson,
        classe_requin=Requin,
        nb_poissons=NOMBRE_INITIAUX_POISSON,
        nb_requins=NOMBRE_INITIAUX_REQUIN,
    )
    print(repr(monde))


if __name__ == "__main__":
    test()
