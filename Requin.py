import parametres
from EtreVivant import EtreVivant
from Poisson import Poisson

class Requin(EtreVivant):
    __energie = parametres.ENERGIE_INITIALE_REQUIN

    @property
    def energie(self) -> int:
        return self.__energie

    @energie.setter
    def energie(self, nouvelle_energie) -> bool:
        self.__energie = nouvelle_energie
        return True

    def __repr__(self) -> str:
        """Affichage terminal

        Returns:
            str: affichage
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

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
        self.energie += parametres.GAIN_ENERGIE_EN_MANGEANT_POISSON
        proie._est_vivant = False
        return True


    def se_reproduire(self):
        # Creation d'un nouveau requin à la même position
        nouveau_requin = Requin(position=self.position)
        
        # Déplacement classique
        self.se_deplacer()

        return nouveau_requin

    def mourir(self):
        if any([self.energie <= 0,
               self.age > parametres.LIMITE_AGE_REQUIN]):
            self.est_vivant = False



# Test conserver temporairement
def test():
    requin = Requin(position=(1,1))
    print(repr(requin))

    poisson = Poisson(position=(1,0))
    print(repr(poisson))
    requin.s_alimenter(poisson)
    print(repr(requin))
    print(repr(poisson))

    nouveau_requin = requin.se_reproduire()
    print(repr(requin))
    print(repr(nouveau_requin))

    nouveau_requin.energie = 0
    nouveau_requin.mourir()
    print(repr(nouveau_requin))
    requin._age = 100
    requin.mourir()
    print(repr(requin))

    print(type(repr(requin)))

if __name__ == "__main__":
    test()


    
