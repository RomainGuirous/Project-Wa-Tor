import parametres
from EtreVivant import EtreVivant

class Poisson(EtreVivant):

    def __init__(self, **kwargs):
        """Constructeur"""
        super().__init__(**kwargs)

    def se_reproduire(self):
        # Creation d'un nouveau poisson à la même position
        nouveau_poisson = Poisson()
        nouveau_poisson.position = self.position.copy()
        
        # Déplacement classique
        self.se_deplacer()

        return nouveau_poisson

    def mourir(self):
        if (self.age > parametres.limite_age_poisson):
            self.estVivant = False


def test():
    poisson = Poisson()
    print(repr(poisson))
    poisson.position = [1,1]
    print(repr(poisson))

    nouveau_poisson = poisson.se_reproduire()
    print(repr(poisson))
    print(repr(nouveau_poisson))

    poisson.age = 50
    poisson.mourir()
    print(repr(poisson))

if __name__ == "__main__":
    test()


    
