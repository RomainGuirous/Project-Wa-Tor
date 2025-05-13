from __future__ import annotations

############################################################
# Pour permettre de lancer les tests...
#######################################
import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
############################################################
from CLASSES.EtreVivant import EtreVivant
from CLASSES.Poisson import Poisson
from CLASSES.Grille import Grille
from parametres import (
    ENERGIE_INITIALE_REQUIN,
    ENERGIE_MAX_REQUIN,
    GAIN_ENERGIE_EN_MANGEANT_POISSON,
    TEMPS_GESTION_REQUIN,
    LIMITE_AGE_REQUIN,
)


class Requin(EtreVivant):
    __energie = ENERGIE_INITIALE_REQUIN
    
    def __init__(self, position, __position_proie = None):
        super().__init__(position)
        self.__position_proie = __position_proie

    @property
    def energie(self) -> int:
        return self.__energie

    def perte_d_energie(self):
        """Perd 1 en energie."""
        self.__energie -= 1

    @property
    def position_proie(self) -> list[tuple[int, int]]:
        return self.__position_proie

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
        self.__energie += min(
            GAIN_ENERGIE_EN_MANGEANT_POISSON, ENERGIE_MAX_REQUIN - self.__energie
        )
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

    def initialiser_traque(self, proie: Requin | Poisson):
        
            

    def __str__(self) -> str:
        """Représentation humainement lisible

        Returns:
            str: affichage
        """
        return super(Requin, self).__str__() + f"energie={self.__energie}\n"


# Test conserver temporairement
def test():
    requin = Requin(position=(1, 1))
    print(f"Requin:\n{str(requin)}")

    poisson = Poisson(position=(1, 0))
    print(f"Poisson:\n{str(poisson)}")
    requin.s_alimenter(poisson.position)
    print(f"Requin:\n{str(requin)}")
    print(f"Poisson:\n{str(poisson)}")

    poisson = Poisson(position=(2, 0))
    print(f"Poisson:\n{str(poisson)}")
    requin.s_alimenter(poisson.position)
    print(f"Requin:\n{str(requin)}")
    print(f"Poisson:\n{str(poisson)}")

    nouveau_requin = requin.se_reproduire()
    print(f"Requin:\n{str(requin)}")
    print(f"Requin:\n{str(nouveau_requin)}")

    nouveau_requin.__energie = 0
    nouveau_requin.mourir()
    print(f"Requin:\n{str(nouveau_requin)}")
    requin._age = 100
    requin.mourir()
    print(f"Requin:\n{str(requin)}")

    print(type(str(requin)))


if __name__ == "__main__":
    test()
