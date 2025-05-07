from monde import Monde
from poisson import Poisson
from requin import Requin
import random

#Classe test pour Poisson
#class Poisson:
    def agir(self, x, y, monde):
        voisins_vides = [pos for pos in monde.voisins(x, y) if monde.lire_case(*pos) is None]
        if voisins_vides:
            nx, ny = random.choice(voisins_vides)
            monde.placer_entite(nx, ny, self)
            monde.placer_entite(x, y, None)

#Classe test pour Requin
#class Requin:
    def agir(self, x, y, monde):
        voisins_vides = [pos for pos in monde.voisins(x, y) if monde.lire_case(*pos) is None]
        if voisins_vides:
            nx, ny = random.choice(voisins_vides)
            monde.placer_entite(nx, ny, self)
            monde.placer_entite(x, y, None)

#Création du monde et initialisation
monde = Monde(colonne=20, ligne=10)
monde.initialiser(nb_poissons=10, nb_requins=5, classe_poisson=Poisson, classe_requin=Requin)

#Exécution de quelques tours de simulation
for _ in range(10):
    monde.afficher()
    monde.executer_chronon()