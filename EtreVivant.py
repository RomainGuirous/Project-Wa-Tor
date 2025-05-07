from random import randint
from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE


class EtreVivant:

    est_vivant = True

    def __init__(self, position: tuple[int, int], age: int = 0) -> None:
        self._position = position
        self._age = age

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    def se_deplacer(self) -> tuple[int, int]:

        directions_possibles = (
            "NSOE"  # création string des directions (Nord, Sud, Ouest, Est)
        )
        direction = directions_possibles[randint(0, 3)]  # une direction au hasard

        # pour chaque modification de la position, on vérifie qu'on reste dans la grille (avec modulo colonne ligne)
        if direction == "N":
            self._position = (
                self._position[0],
                (self._position[1] + 1) % NOMBRE_LIGNE_GRILLE,
            )
        if direction == "S":
            self._position = (
                self._position[0],
                (self._position[1] - 1) % NOMBRE_LIGNE_GRILLE,
            )
        if direction == "O":
            self._position = (
                (self._position[0] + 1) % NOMBRE_COLONNE_GRILLE,
                self._position[1],
            )
        if direction == "E":
            self._position = (
                (self._position[0] - 1) % NOMBRE_COLONNE_GRILLE,
                self._position[1],
            )

    @property
    def age(self) -> int:
        return self._age

    def se_reproduire():
        pass

    def s_alimenter():
        pass

    def vieillir(self) -> int:

        self._age += 1

    def __repr__(self) -> str:
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
