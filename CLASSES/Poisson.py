from __future__ import annotations
from parametres import TEMPS_GESTION_POISSON, LIMITE_AGE_POISSON
from CLASSES.EtreVivant import EtreVivant


class Poisson(EtreVivant):

    def vieillir(self, temps_reproduction=TEMPS_GESTION_POISSON) -> None:
        """
        Vieillit le poisson d'un an et gère la reproduction si le poisson est enceinte.

        Args:
            temps_reproduction (int): Temps nécessaire pour que le poisson puisse se reproduire.

        Returns:
            None
        """
        return super().vieillir(temps_reproduction)

    def mourir(self, age_max: int = LIMITE_AGE_POISSON) -> None:
        """
        Indique la mort du poisson si il a dépassé l'âge maximum ou si il n'est plus vivant.

        Args:
            age_max (int): Âge maximum du poisson.

        Returns:
            None
        """
        super().mourir(age_max)

class SuperPoisson(Poisson):
    pass


def test():
    poisson = Poisson(position=(1, 1))
    print(repr(poisson))

    nouveau_poisson = poisson.se_reproduire()
    print(repr(poisson))
    print(repr(nouveau_poisson))

    poisson._age = 50
    poisson.mourir()
    print(repr(poisson))


if __name__ == "__main__":
    test()
