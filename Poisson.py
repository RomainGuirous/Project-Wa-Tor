from __future__ import annotations
import parametres
from EtreVivant import EtreVivant


class Poisson(EtreVivant):
    age_reproduction = parametres.AGE_REPRODUCTION_POISSON

    def se_reproduire(
        self, liste_deplacements_disponibles: list[tuple[int, int]]
    ) -> Poisson:
        """Se déplace et laisse un nouveau poisson derrière lui.

        Returns:
            Poisson: Le nouveau poisson
        """
        # Creation d'un nouveau poisson à la même position
        nouveau_poisson = Poisson(self.position)

        # Déplacement classique
        self.se_deplacer(liste_deplacements_disponibles)

        return nouveau_poisson

    def mourir(self):
        """Indique la mort du poisson"""
        if self.age > parametres.LIMITE_AGE_POISSON:
            self._est_vivant = False


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
