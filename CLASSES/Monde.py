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
from rich.emoji import Emoji
from CLASSES.Grille import Grille
from CLASSES.Poisson import Poisson
from CLASSES.Requin import Requin
from parametres import (
    NOMBRE_LIGNE_GRILLE,
    NOMBRE_COLONNE_GRILLE,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_REQUIN,
    TEMPS_RAFRAICHISSEMENT,
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
        if (nb_poissons < 0):
            raise ValueError("Le nombre de poissons initial doit être positif.")
        if (nb_requins < 0):
            raise ValueError("Le nombre de requins initial doit être positif.")
        self.est_suffisamment_grand(nb_poissons+nb_requins)

        # Liste aléatoires de toutes les positions de la grille
        toutes_les_positions = self.toutes_les_positions()
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
    def placer_une_espece(self, classe_espece: Poisson | Requin, nb_entites: int, positions_possibles: list[tuple[int, int]]) -> None:
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
            if entite == None:
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
            if entite is None:
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

    def executer_toutes_les_actions_des_requins(self, toutes_les_positions:list[tuple[int,int]], deja_agis: list) -> None:
        """Exécute toutes les actions des requins dans le monde.
        Chaque requin peut se reproduire, manger ou se déplacer, en fonction des possibilités offertes par les case voisines.
        Les requins agissent dans un ordre aléatoire pour simuler le comportement du monde.

        Args:
            toutes_les_positions (list[tuple[int,int]]): Toutes les positions qui n'ont pas encore été inspectées pour action à ce chronon.
            deja_agis (list): Liste des positions des entités qui ont déjà agis durant ce chronon.
        """

        for position in toutes_les_positions:
            entite = self.grille.lire_case(position)

            if any([entite is None,
                    not isinstance(entite, Requin),
                    position in deja_agis
            ]):
                continue

            # Liste des positions des cases voisines
            voisins = self.grille.cases_voisines(position)

            # Trouver les cases vides autour
            cases_vides = self.grille.cases_libres(position)

            # Trouver les poissons autour
            cases_poissons = [
                voisin
                for voisin in voisins
                if self.grille.lire_case(voisin)
                and isinstance(self.grille.lire_case(voisin), Poisson)
            ]

            # S'il y a au moins une case vide autour:
            if len(cases_vides) > 0:
                # Un requin se reproduit en priorité
                if entite._est_enceinte:
                    bebe = entite.se_reproduire(cases_vides) 
                    # entite a changé de position
                    self.grille.placer_entite(position, bebe)
                    self.grille.placer_entite(entite.position, entite)
                    deja_agis.append(entite.position)

                # Sinon, s’il peut manger un poisson, il le fait
                elif len(cases_poissons) > 0:
                    cible = random.choice(cases_poissons)
                    position_avant = entite.position
                    entite.s_alimenter(cible)  # change de position
                    self.grille.placer_entite(entite.position, entite)
                    self.grille.placer_entite(position_avant, None)
                    deja_agis.append(cible)

                # Sinon, il se déplace aléatoirement
                else:
                    position_avant = entite.position
                    entite.se_deplacer(cases_vides)  # change de position
                    self.grille.placer_entite(entite.position, entite)
                    self.grille.placer_entite(position_avant, None)
                    deja_agis.append(entite.position)

            # S'il n'y a aucune case vide autour...
            else:
                # ...mais qu'il y a au moins un poisson:
                # Un requin mange en priorité
                if len(cases_poissons) > 0:
                    cible = random.choice(cases_poissons)
                    position_avant = entite.position
                    entite.s_alimenter(cible)  # change de position
                    self.grille.placer_entite(entite.position, entite)
                    self.grille.placer_entite(position_avant, None)
                    deja_agis.append(cible)

                # Sinon il ne bouge pas (bloqué)

    def executer_toutes_les_actions_des_poissons(self, toutes_les_positions:list[tuple[int,int]], deja_agis: list) -> None:
        """Exécute toutes les actions des poissons dans le monde.
        Chaque poisson peut se reproduire, manger ou se déplacer, en fonction des possibilités offertes par les case voisines.
        Les poissons agissent dans un ordre aléatoire pour simuler le comportement du monde.

        Args:
            toutes_les_positions (list[tuple[int,int]]): Toutes les positions qui n'ont pas encore été inspectées pour action à ce chronon.
            deja_agis (list): Liste des positions des entités qui ont déjà agis durant ce chronon.
        """

        for position in toutes_les_positions:
            entite = self.grille.lire_case(position)

            if any([entite is None,
                    not isinstance(entite, Poisson),
                    position in deja_agis
                    ]):
                continue

            # Liste des positions des cases voisines
            #voisins = self.grille.cases_voisines(position)

            # Trouver les cases vides
            cases_vides = self.grille.cases_libres(position)

            # S'il y a au moins une case vide autour:
            if len(cases_vides) > 0:
                # Un poisson se reproduit en priorité
                if entite._est_enceinte:
                    bebe = entite.se_reproduire(cases_vides)
                    # entite a changé de position
                    self.grille.placer_entite(position, bebe)
                    self.grille.placer_entite(entite.position, entite)
                    deja_agis.append(entite.position)

                # Sinon, il se déplace aléatoirement
                else:
                    position_avant = entite.position
                    entite.se_deplacer(cases_vides)  # change de position
                    self.grille.placer_entite(entite.position, entite)
                    self.grille.placer_entite(position_avant, None)
                    deja_agis.append(entite.position)
            
            # Sinon il ne bouge pas (bloqué)
    
        
    # region Méthode: afficher
    def afficher(self) -> None:
        """
        Affiche la grille du monde avec les entités présentes.
        Chaque case est représentée par un emoji correspondant à l'entité présente.
        Les cases vides sont représentées par un emoji d'eau.
        Les poissons et requins sont représentés par leurs emojis respectifs.

        Returns:
            None: Affiche la grille dans le terminal.
        """
        for y in range(self.lignes):
            ligne_separateur = "+"
            ligne = "|"
            for x in range(self.colonnes):
                entite = self.grille.lire_case((x, y))
                if entite is None:
                    # ligne += Emoji.replace(":water_wave:")  # case vide 🌊
                    ligne += Emoji.replace(":blue_square:")  # case vide 🟦
                    # ligne += Emoji.replace(":black_large_square:")  # case vide ⬛
                    # ligne += Emoji.replace(":blue_circle:")  # case vide 🔵
                    # ligne += Emoji.replace(":droplet:")  # case vide 💧
                    # ligne += Emoji.replace(":large_blue_diamond:")  # case vide 🔷
                    # ligne += Emoji.replace(":sweat_droplets:")  # case vide 💦
                elif isinstance(entite, Poisson):
                    # ligne += Emoji.replace(":fish:") # poisson 🐟
                    ligne += Emoji.replace(":tropical_fish:")  # poisson tropical 🐠
                    # ligne += Emoji.replace(":blowfish:") # poisson ballon 🐡
                elif isinstance(entite, Requin):
                    ligne += Emoji.replace(":shark:")  # requin 🦈
                else:
                    ligne += Emoji.replace(
                        ":grey_question:"
                    )  # point d'interrogation ❔
                    # ligne += Emoji.replace(":white_question_mark:") #point d'interrogation ❔
                    # ligne += Emoji.replace(":boat:")  # bateau ⛵
                    # ligne += Emoji.replace(":speedboat:")  # bateau 🚤
                    # ligne += Emoji.replace(":crab:")  # crabe 🦀
                    # ligne += Emoji.replace(":diving_mask:")  # plongeur 🤿
                    # ligne += Emoji.replace(":dolphin:")  # dauphin 🐬
                    # ligne += Emoji.replace(":flipper:")  # dauphin 🐬
                    # ligne += Emoji.replace(":ice:")  # iceberg 🧊
                    # ligne += Emoji.replace(":lobster:")  # iceberg 🦞
                    # ligne += Emoji.replace(":white_circle:")  # rocher ⚪
                    # ligne += Emoji.replace(":whale:")  # baleine 🐳
                    # ligne += Emoji.replace(":whale:")  # baleine 🐋
                    # ligne += Emoji.replace(":turtle:")  # tortue 🐢
                    # ligne += Emoji.replace(":surfer:")  # surfer 🏄
                    # ligne += Emoji.replace(":shrimp:")  # crevette 🦐
                    # ligne += Emoji.replace(":rowboat:")  # canoe 🚣
                    # ligne += Emoji.replace(":octopus:")  # pieuvre 🐙
                    # ligne += Emoji.replace(":microbe:")  # microbe 🦠
                    # ligne += Emoji.replace(":mermaid:")  # sirène 🧜‍
                    # ligne += Emoji.replace(":black_square_button:") # rocher 🔲
                    # ligne += Emoji.replace(":white_large_square_button:") # rocher ⬜

                ligne_separateur += "--+"
                ligne += "|"

            if y == 0:
                print("+--------------+")
                print("| WA-TOR WORLD |")
                print("+--------------+\n")
                print(f"Chronon: {self.chronon}\n")

            print(ligne_separateur)
            print(ligne)
        else:
            print(ligne_separateur)

        sleep(TEMPS_RAFRAICHISSEMENT)

    # region REPR

    def __repr__(self) -> str:
        """
        Affichage terminal
        """
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"


# region TEST


def test():
    # Création du monde et initialisation
    monde = Monde()
    monde.initialiser(
        classe_poisson=Poisson,
        classe_requin=Requin,
        nb_poissons=NOMBRE_INITIAUX_POISSON,
        nb_requins=NOMBRE_INITIAUX_REQUIN,
    )

    print(repr(monde))

    # for _ in range(10):
    #     # Rafraichir le terminal (cls pour windows et clear pour linux)
    #     os.system("cls" if os.name == "nt" else "clear")

    #     # Affichage de la grille (avec en-tete)
    #     monde.afficher()
    #     monde.executer_chronon()

    #     # Attendre 2 sec
    #     time.sleep(2)


# if __name__ == "__main__":
#    test()
