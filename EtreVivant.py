from random import randint
from Grille import Grille


class EtreVivant:

    _est_vivant = True
    _age = 0

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
            None
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

    def se_reproduire():
        pass

    def s_alimenter():
        pass

    def vieillir(self) -> None:
        """
        Vieillit l'entité d'un an.
        """
        self._age += 1

    def mourir():
        pass

    def __repr__(self) -> str:
        """
        Affichage terminal
        """
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
