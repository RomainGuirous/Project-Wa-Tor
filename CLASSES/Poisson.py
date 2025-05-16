from parametres import TEMPS_GESTION_POISSON, LIMITE_AGE_POISSON
from CLASSES.EtreVivant import EtreVivant


class Poisson(EtreVivant):

    def vieillir(self, temps_reproduction=TEMPS_GESTION_POISSON) -> None:
        """
        Vieillit le poisson d'un an et indique si le poisson devient enceinte.

        Args:
            temps_reproduction (int, optionel): Temps nécessaire pour que le poisson puisse se reproduire.
            Valeur par défaut: TEMPS_GESTION_POISSON

        Returns:
            None
        """
        return super().vieillir(temps_reproduction)

    def mourir(self, age_max: int = LIMITE_AGE_POISSON) -> None:
        """
        Indique la mort du poisson si il a dépassé l'âge maximum.

        Args:
            age_max (int, optionel): Âge maximum du poisson. Valeur par défaut: LIMITE_AGE_POISSON.

        Returns:
            None
        """
        super().mourir(age_max)


class SuperPoisson(Poisson):
    # Un super poisson n'a pas de nouvel attribut ou méthode mais est
    # traité légèrement différemment dans Monde.py
    pass


def test():
    # Test initialisation
    poisson = Poisson(position=(1, 1))
    print(repr(poisson))

    # Test se reproduire
    nouveau_poisson = poisson.se_reproduire()
    print(repr(poisson))
    print(repr(nouveau_poisson))

    # Test mourir
    poisson._age = 50
    poisson.mourir()
    print(repr(poisson))


if __name__ == "__main__":
    test()
