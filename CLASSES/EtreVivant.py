from typing import Self  # Pour le type hinting de la méthode se_reproduire
from random import randint
from CLASSES.Grille import Grille


class EtreVivant:

    _est_vivant = True
    _age = 0
    _temps_gestion = 0
    _est_enceinte = False

    def __init__(self, position: tuple[int, int]) -> None:
        """
        Constructeur de la classe EtreVivant.
        Initialise l'entité avec une position donnée.
        """
        self._position = position

    @property
    def position(self) -> tuple[int, int]:
        """
        Renvoie la position de l'entité.
        La position est un tuple (x, y) représentant les coordonnées de l'entité dans la grille.
        """
        return self._position

    def se_deplacer(
        self, liste_deplacements_disponibles: list[tuple[int, int]] = []
    ) -> None:
        """
        Déplace l'entité vers une position aléatoire parmi les positions disponibles.
        Si aucune position n'est fournie, utilise la grille pour trouver les positions libres.
        Si aucune position n'est disponible, l'entité ne se déplace pas.
        Args:
            liste_deplacements_disponibles (list[tuple[int, int]], optional): Liste des positions disponibles. Par défaut -> [].

        Returns:
            None: L'entité se déplace vers une position aléatoire parmi les positions disponible et met à jour sa position.
        """
        if not liste_deplacements_disponibles:
            grille = Grille()
            liste_deplacements_disponibles = grille.cases_libres(self.position)

        hasard = randint(0, len(liste_deplacements_disponibles) - 1)
        self._position = liste_deplacements_disponibles[hasard]

    @property
    def age(self) -> int:
        """
        Renvoie l'âge de l'entité.
        L'âge est un entier représentant le nombre d'années depuis la naissance de l'entité.
        """
        return self._age

    @property
    def est_vivant(self) -> bool:
        return self._est_vivant

    def se_reproduire(
        self, liste_deplacements_disponibles: list[tuple[int, int]] = []
    ) -> Self:
        """
        Se déplace et laisse un nouvel être vivant derrière lui.

        Args:
            liste_deplacements_disponibles (list[tuple[int, int]], optional): Liste des positions disponibles pour le déplacement.
            Par défault égal à [].

        Returns:
            EtreVivant: Le nouvel être vivant
        """
        # Si aucune position n'est fournie, utilise la grille pour trouver les positions libres
        if not liste_deplacements_disponibles:
            grille = Grille()
            liste_deplacements_disponibles = grille.cases_libres(self.position)

        # Creation d'un nouveau être vivant à la même position (les classes filles créront leur propre instance)
        nouveau_vivant = self.__class__(self.position)

        # Déplacement classique
        self.se_deplacer(liste_deplacements_disponibles)

        # Réinitialisation de l'état enceinte
        self._est_enceinte = False

        return nouveau_vivant

    def s_alimenter():
        pass

    def vieillir(self, temps_reproduction: int) -> None:
        """
        Vieillit l'entité d'un an et gère la reproduction si l'entité est enceinte.

        Args:
            temps_reproduction (int): Temps nécessaire pour que l'entité puisse se reproduire.

        Returns:
            None
        """
        self._age += 1
        if not self._est_enceinte:
            self._temps_gestion += 1
            if self._temps_gestion >= temps_reproduction:
                self._est_enceinte = True
                self._temps_gestion = 0

    def mourir(self, age_max: int) -> None:
        """
        Indique la mort de l'entité si elle a dépassé l'âge maximum ou si elle n'est plus vivante.

        Args:
            age_max (int): Âge maximum de l'entité.

        Returns:
            None
        """
        if self.age > age_max:
            self._est_vivant = False

    def __repr__(self) -> str:
        """
        Affichage terminal
        """
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

    def __str__(self) -> str:
        """Représentation humainement lisible.

        Returns:
            str: affichage
        """
        return f"est_vivant={self._est_vivant}\n" + \
               f"age={self.age}\n" + \
               f"position={self.position}\n" + \
               f"temps gestion={self._temps_gestion}\n" + \
               f"est_enceinte={self._est_enceinte}\n"
    
if __name__ == "__main__":
    # Code à exécuter uniquement si ce fichier est lancé directement
    print("Ce fichier est conçu pour être importé, pas exécuté directement.")

