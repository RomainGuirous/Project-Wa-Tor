from __future__ import annotations
from CLASSES.EtreVivant import EtreVivant
from parametres import (
    ENERGIE_INITIALE_REQUIN,
    GAIN_ENERGIE_EN_MANGEANT_POISSON,
    TEMPS_GESTION_REQUIN,
    LIMITE_AGE_REQUIN,
)


class Requin(EtreVivant):
    __energie = ENERGIE_INITIALE_REQUIN

    @property
    def energie(self) -> int:
        return self.__energie

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

    def vieillir(self, temps_reproduction: int = TEMPS_GESTION_REQUIN) -> None:
        """
        Vieillit le requin d'un an et gère la reproduction si le requin est enceinte.

        Args:
            temps_reproduction (int): Temps nécessaire pour que le requin puisse se reproduire.

        Returns:
            None
        """
        # Vieillit le requin
        super().vieillir(temps_reproduction)
        # Perte d'énergie
        self.perte_d_energie()

    def mourir(self, age_max: int = LIMITE_AGE_REQUIN) -> None:
        """
        Indique la mort du requin si il a dépassé l'âge maximum ou si il n'a plus d'énergie.

        Args:
            age_max (int): Âge maximum du requin.

        Returns:
            None
        """
        # Si le requin n'a plus d'énergie, il meurt
        if self.__energie <= 0:
            self._est_vivant = False
            return
        # Si le requin a dépassé l'âge maximum, il meurt
        super().mourir(age_max)


# Test conserver temporairement
def test():
    requin = Requin(position=(1, 1))
    print(repr(requin))


if __name__ == "__main__":
    test()
