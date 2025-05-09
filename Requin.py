from __future__ import annotations
from EtreVivant import EtreVivant
from Poisson import Poisson
from parametres import (
    ENERGIE_INITIALE_REQUIN,
    AGE_REPRODUCTION_REQUIN,
    GAIN_ENERGIE_EN_MANGEANT_POISSON,
    LIMITE_AGE_REQUIN,
)


class Requin(EtreVivant):
    __energie = ENERGIE_INITIALE_REQUIN
    age_reproduction = AGE_REPRODUCTION_REQUIN

    @property
    def energie(self) -> int:
        return self.__energie

    def __repr__(self) -> str:
        """Affichage terminal

        Returns:
            str: affichage
        """
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

    def perte_d_energie(self):
        """Perd 1 en energie."""
        self.__energie -= 1

    def s_alimenter(self, position_proie: tuple[int, int]) -> bool:
        """
        se déplace à la position de la proie et
        l'élimine pour gagner de l'énergie

        Args:
            proie (Poisson): le poisson qui sera mangé

        Returns:
            bool: le poisson a-t-il été mangé ?
        """
        # Déplacement vers la proie
        self._position = position_proie

        # Mange la proie
        self.__energie += GAIN_ENERGIE_EN_MANGEANT_POISSON
        # proie._est_vivant = False
        return True

    def se_reproduire(
        self, liste_deplacements_disponibles: list[tuple[int, int]]
    ) -> Requin:

        if self.__est_enceinte:
            # Creation d'un nouveau requin à la même position
            nouveau_requin = Requin(self.position)

            # Déplacement classique
            self.se_deplacer(liste_deplacements_disponibles)

            # Réinitialisation de l'état enceinte
            self.__est_enceinte = False

            return nouveau_requin
        else:
            pass

    def mourir(self):
        if any([self.energie <= 0, self.age > LIMITE_AGE_REQUIN]):
            self._est_vivant = False


# Test conserver temporairement
def test():
    requin = Requin(position=(1, 1))
    print(repr(requin))

    poisson = Poisson(position=(1, 0))
    print(repr(poisson))
    requin.s_alimenter(poisson)
    print(repr(requin))
    print(repr(poisson))

    nouveau_requin = requin.se_reproduire()
    print(repr(requin))
    print(repr(nouveau_requin))

    nouveau_requin.__energie = 0
    nouveau_requin.mourir()
    print(repr(nouveau_requin))
    requin._age = 100
    requin.mourir()
    print(repr(requin))

    print(type(repr(requin)))


if __name__ == "__main__":
    test()
