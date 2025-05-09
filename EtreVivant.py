from random import randint
from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE
import Grille as Grille


class EtreVivant:

    _est_vivant = True
    _age = 0

    def __init__(self, position: tuple[int, int] = (0,0)) -> None:
        self._position = position

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    def se_deplacer(self, liste_deplacements_disponibles: list[tuple[int, int]]=[]) -> None:
    
        if not liste_deplacements_disponibles:
            grille = Grille.Grille()
            liste_deplacements_disponibles = grille.cases_libres(self.position)

        hasard = randint(0, len(liste_deplacements_disponibles) -1)
        self._position = liste_deplacements_disponibles[hasard]


    @property
    def age(self) -> int:
        return self._age

    def se_reproduire():
        pass

    def s_alimenter():
        pass

    def vieillir(self) -> int:

        self._age += 1

    def mourir():
        pass

    def __repr__(self) -> str:
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
    
test = EtreVivant()
test._age = 1
print(test.age)
print(repr(test))