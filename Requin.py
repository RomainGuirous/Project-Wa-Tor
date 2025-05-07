import parametres
from EtreVivant import EtreVivant
from Poisson import Poisson

class Requin(EtreVivant):
    def __init__(self, **kwargs):
        """Constructeur"""
        super().__init__(**kwargs)
        self.energie = parametres.energie_requin


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
        self.position = proie.position

        # Mange la proie
        self.energie += parametres.gain_energie_en_mangeant_poisson
        proie.estVivant = False
        return True


    def se_reproduire(self):
        # Creation d'un nouveau requin à la même position
        nouveau_requin = Requin()
        nouveau_requin.position = self.position.copy()
        
        # Déplacement classique
        self.se_deplacer()

        return nouveau_requin

    def mourir(self):
        if any([self.energie <= 0,
               self.age > parametres.limite_age_requin]):
            self.estVivant = False

def test():
    requin = Requin()
    print(repr(requin))
    requin.position = [1,1]
    print(repr(requin))

    poisson = Poisson()
    print(repr(poisson))
    poisson.position = [1,0]
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
    requin.age = 100
    requin.mourir()
    print(repr(requin))

    print(type(repr(requin)))

if __name__ == "__main__":
    test()


    
