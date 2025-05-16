from __future__ import (
    annotations,
)  # Pour indiquer la classe de self à une autre paramètre dans le type hinting

############################################################
# Pour permettre de lancer les tests...
#######################################
import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
############################################################
import random

random.seed()

from CLASSES.EtreVivant import EtreVivant
from CLASSES.Poisson import Poisson
from parametres import (
    ENERGIE_INITIALE_REQUIN,
    ENERGIE_MAX_REQUIN,
    GAIN_ENERGIE_EN_MANGEANT_POISSON,
    TEMPS_GESTION_REQUIN,
    LIMITE_AGE_REQUIN,
    PERTE_ENERGIE_EN_COMBATTANT,
    AGE_ADULTE_REQUIN,
)


class Requin(EtreVivant):
    __energie = ENERGIE_INITIALE_REQUIN
    _est_bebe = True  # Pour épargner les bébés dans la phase de combat

    @property
    def energie(self) -> int:
        """Renvoie le niveau d'énergie du requin"""
        return self.__energie

    @property
    def est_bebe(self) -> bool:
        """
        Renvoie un booléen indiquant si l'entité est un bebe.
        """
        return self._est_bebe

    def perte_d_energie(self) -> None:
        """Perd 1 en energie."""
        self.__energie -= 1

    def s_alimenter(self, position_proie: tuple[int, int]) -> bool:
        """
        se déplace à la position de la proie et
        l'élimine pour gagner de l'énergie.

        Args:
            position_proie (tuple[int, int]): Position de la proie sur la grille

        Returns:
            bool: La proie a-t-elle été mangé ?
        """

        # Déplacement vers la proie
        self._position = position_proie

        # Mange la proie
        self.__energie += min(
            GAIN_ENERGIE_EN_MANGEANT_POISSON, ENERGIE_MAX_REQUIN - self.__energie
        )
        return True

    def combattre(self, adversaire: Requin) -> bool:
        """
        combat avec un autre requin. Le résultat du combat est aléatoire.
        L'un des deux requins meurent, l'autre prend sa position et perd
        de l'énergie.

        Args:
            adversaire (Requin): l'autre requin

        Returns:
            bool: True si self a gagné, False si adversaire a gagné
        """
        # Victoire de self ?
        est_victorieux = random.choice([True, False])

        if est_victorieux:
            # Déplacement vers l'adversaire éliminé
            self._position = adversaire._position
            adversaire._est_vivant = False

            # Perte d'énergie en raison des blessures
            self.__energie -= PERTE_ENERGIE_EN_COMBATTANT
        else:
            # Déplacement de l'adversaire vers le requin éliminé
            adversaire._position = self._position
            self._est_vivant = False

            # Perte d'énergie en raison des blessures
            adversaire.__energie -= PERTE_ENERGIE_EN_COMBATTANT

        return False

    def vieillir(self, temps_reproduction: int = TEMPS_GESTION_REQUIN) -> None:
        """
        Vieillit le requin d'un chronon, lui fait perd 1 d'énergie,
        indique si le requin devient enceinte et gère le passage à
        l'âge adulte.

        Args:
            temps_reproduction (int, optionel): Temps nécessaire pour que le requin puisse se reproduire.
            Default est à TEMPS_GESTION_REQUIN

        Returns:
            None
        """
        # Vieillit le requin en tant qu'être vivant
        super().vieillir(temps_reproduction)
        # Perte d'énergie
        self.perte_d_energie()
        # Passage à l'age adulte
        if self.age >= AGE_ADULTE_REQUIN:
            self._est_bebe = False

    def mourir(self, age_max: int = LIMITE_AGE_REQUIN) -> None:
        """
        Indique la mort du requin si il a dépassé l'âge maximum ou si il n'a plus d'énergie.

        Args:
            age_max (int, optionel): Âge maximum du requin. Par défaut est à LIMITE_AGE_REQUIN.

        Returns:
            None
        """
        # Si le requin n'a plus d'énergie, il meurt
        if self.__energie <= 0:
            self._est_vivant = False
            return
        # Si le requin a dépassé l'âge maximum, il meurt
        super().mourir(age_max)

    def __str__(self) -> str:
        """Représentation humainement lisible

        Returns:
            str: La représentation
        """
        return (
            super(Requin, self).__str__()
            + f"est_bebe={self._est_bebe}\n"
            + f"energie={self.__energie}\n"
        )


# Test
def test():
    # Test initialisation
    requin = Requin(position=(1, 1))
    print(f"Requin:\n{str(requin)}")

    # Test s'alimenter
    poisson = Poisson(position=(1, 0))
    print(f"Poisson:\n{str(poisson)}")
    requin.s_alimenter(poisson.position)
    print(f"Requin:\n{str(requin)}")
    print(f"Poisson:\n{str(poisson)}")

    # Test s'alimenter
    poisson = Poisson(position=(2, 0))
    print(f"Poisson:\n{str(poisson)}")
    requin.s_alimenter(poisson.position)
    print(f"Requin:\n{str(requin)}")
    print(f"Poisson:\n{str(poisson)}")

    # Test se reproduire
    nouveau_requin = requin.se_reproduire()
    print(f"Requin:\n{str(requin)}")
    print(f"Requin:\n{str(nouveau_requin)}")

    # Test vieillir
    while requin.est_bebe:
        requin.vieillir()
        print(f"Requin:\n{str(requin)}")

    # Test mourir
    nouveau_requin.__energie = 0
    nouveau_requin.mourir()
    print(f"Requin:\n{str(nouveau_requin)}")
    requin._age = 100
    requin.mourir()
    print(f"Requin:\n{str(requin)}")

    # Test type
    print(type(str(requin)))

    # Test combattre
    requin1 = Requin(position=(1, 1))
    print(f"Requin1:\n{str(requin1)}")
    requin2 = Requin(position=(2, 1))
    print(f"Requin2:\n{str(requin2)}")
    requin1.combattre(requin2)
    print(f"Requin1:\n{str(requin1)}")
    print(f"Requin2:\n{str(requin2)}")


if __name__ == "__main__":
    test()
