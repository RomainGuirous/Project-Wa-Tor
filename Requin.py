from __future__ import annotations
from parametres import (
    ENERGIE_INITIALE_REQUIN,
    ENERGIE_MAX_REQUIN,
    GAIN_ENERGIE_EN_MANGEANT_POISSON,
    LIMITE_AGE_REQUIN,
)
from EtreVivant import EtreVivant
from Poisson import Poisson


class Requin(EtreVivant):
    __energie = ENERGIE_INITIALE_REQUIN

    @property
    def energie(self) -> int:
        return self.__energie

    def __str__(self) -> str:
        """Représentation officielle

        Returns:
            str: affichage
        """
        return super(Requin, self).__str__() + f"energie={self.__energie}\n"

    def __repr__(self) -> str:
        """Représentation officielle

        Returns:
            str: affichage
        """
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

    def perte_d_energie(self):
        """Perd 1 en energie."""
        self.__energie -= 1

    def s_alimenter(self, proie: Poisson) -> bool:
        """se déplace à la position de la proie et
        l'élimine pour gagner de l'énergie

        Args:
            proie (Poisson): le poisson qui sera mangé

        Returns:
            bool: le poisson a-t-il été mangé ?
        """
        # Déplacement vers la proie
        self._position = proie.position

        # Mange la proie
        self.__energie += min(
            GAIN_ENERGIE_EN_MANGEANT_POISSON, ENERGIE_MAX_REQUIN - self.__energie
        )
        proie._est_vivant = False
        return True

    def se_reproduire(self) -> Requin:
        # Creation d'un nouveau requin à la même position
        nouveau_requin = Requin(position=self.position)

        # Déplacement classique
        self.se_deplacer()

        return nouveau_requin

    def mourir(self):
        if any([self.energie <= 0, self.age > LIMITE_AGE_REQUIN]):
            self._est_vivant = False


# Test conserver temporairement
def test():
    requin = Requin(position=(1, 1))
    print(str(requin))

    poisson = Poisson(position=(1, 0))
    print(str(poisson))
    requin.s_alimenter(poisson)
    print(str(requin))
    print(str(poisson))

    poisson = Poisson(position=(2, 0))
    print(str(poisson))
    requin.s_alimenter(poisson)
    print(str(requin))
    print(str(poisson))

    nouveau_requin = requin.se_reproduire()
    print(str(requin))
    print(str(nouveau_requin))

    nouveau_requin.__energie = 0
    nouveau_requin.mourir()
    print(str(nouveau_requin))
    requin._age = 100
    requin.mourir()
    print(str(requin))

    print(type(str(requin)))


if __name__ == "__main__":
    test()
