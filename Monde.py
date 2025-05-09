import random
import parametres
from Poisson import Poisson
from Requin import Requin
from Grille import Grille
from parametres import NOMBRE_COLONNE_GRILLE, NOMBRE_LIGNE_GRILLE

class Monde:
    def __init__(self):
        self.grille = Grille(NOMBRE_COLONNE_GRILLE, NOMBRE_LIGNE_GRILLE)
        self.chronon = 0
        self.colonnes = NOMBRE_COLONNE_GRILLE
        self.lignes = NOMBRE_LIGNE_GRILLE

    def initialiser(self, nb_poissons, nb_requins, classe_poisson, classe_requin):
        toutes_les_positions = [(x, y) for x in range(self.colonnes) for y in range(self.lignes)]
        random.shuffle(toutes_les_positions)

        for _ in range(nb_poissons):
            if not toutes_les_positions:
                break
            x, y = toutes_les_positions.pop()
            poisson = classe_poisson(position=(x, y))
            self.grille.placer_entite(x, y, poisson)

        for _ in range(nb_requins):
            if not toutes_les_positions:
                break
            x, y = toutes_les_positions.pop()
            requin = classe_requin(position=(x, y))
            self.grille.placer_entite(x, y, requin)

    def executer_chronon(self):
        toutes_les_positions = [(x, y) for x in range(self.colonnes) for y in range(self.lignes)]
        random.shuffle(toutes_les_positions)

        for x, y in toutes_les_positions:
            entite = self.grille.lire_case(x, y)
            if entite is None:
                continue

            ancienne_position = entite.position
            entite.vieillir()
            entite.mourir()

            if not entite._est_vivant:
                self.grille.placer_entite(*ancienne_position, None)
                continue


            if entite.age >= parametres.TEMPS_REPRODUCTION_POISSON:
                bebe = entite.se_reproduire()
                self.grille.placer_entite(*ancienne_position, bebe)
                entite._age = 0


            entite.se_deplacer()
            nouvelle_position = entite.position

            if self.grille.lire_case(*nouvelle_position) is None:
                self.grille.placer_entite(*nouvelle_position, entite)
                self.grille.placer_entite(*ancienne_position, None)

        self.chronon += 1

    def afficher(self):
        for y in range(self.lignes):
            ligne = ""
            for x in range(self.colonnes):
                entite = self.grille.lire_case(x, y)
                if entite is None:
                    ligne += "."
                elif entite.__class__.__name__.lower() == "poisson":
                    ligne += "P"
                elif entite.__class__.__name__.lower() == "requin":
                    ligne += "R"
                else:
                    ligne += "?"
            print(ligne)
        print("Chronon :", self.chronon)
        print()

def test():
    monde = Monde()
    monde.initialiser(nb_poissons=10, nb_requins=5, classe_poisson=Poisson, classe_requin=Requin)

    for _ in range(10):
        monde.afficher()
        monde.executer_chronon()

if __name__ == "__main__":
    test()
