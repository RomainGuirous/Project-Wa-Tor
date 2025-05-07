import random  # Pour utiliser le mélange aléatoire des positions

random.seed()
from Poisson import Poisson
from Requin import Requin


# Classe qui représente le monde Wa-Tor
class Monde:
    __chronon = 0  # Compteur de temps

    # Initialisation du monde avec une largeur (colonne) et une hauteur (ligne)
    def __init__(self, colonne, ligne):
        self.colonne = colonne
        self.ligne = ligne

        # Création d'une grille vide (liste de listes), avec None dans chaque case
        self.grille = []
        for y in range(ligne):
            ligne_grille = []
            for x in range(colonne):
                ligne_grille.append(None)
            self.grille.append(ligne_grille)

    # Récupérer ce qu'il y a dans une case, avec rebouclage si on dépasse
    def lire_case(self, x, y):
        x = x % self.colonne
        y = y % self.ligne
        return self.grille[y][x]

    # Placer une entité dans une case (rebouclage aussi)
    def placer_entite(self, x, y, entite):
        x = x % self.colonne
        y = y % self.ligne
        self.grille[y][x] = entite

    # Donne les coordonnées des cases voisines (haut, bas, gauche, droite)
    # def voisins(self, x, y):
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     voisins = []
    #     for dx, dy in directions:
    #         nx = (x + dx) % self.colonne
    #         ny = (y + dy) % self.ligne
    #         voisins.append((nx, ny))
    #     return voisins

    # Place aléatoirement les poissons et les requins dans la grille
    def initialiser(self, nb_poissons, nb_requins, classe_poisson, classe_requin):
        # On crée une liste de toutes les positions possibles
        positions = [(x, y) for x in range(self.colonne) for y in range(self.ligne)]
        random.shuffle(positions)  # Mélange les positions pour placer au hasard

        # Placement des poissons
        for _ in range(nb_poissons):
            if not positions:
                break  # plus de place
            x, y = positions.pop()
            poisson = Poisson((x, y))
            self.placer_entite(x, y, poisson)

        # Placement des requins
        for _ in range(nb_requins):
            if not positions:
                break
            x, y = positions.pop()
            requin = Requin((x, y))
            self.placer_entite(x, y, requin)

    # Exécute un tour de simulation (chronon)
    def executer_chronon(self):
        # On récupère toutes les positions de la grille
        positions = [(x, y) for x in range(self.colonne) for y in range(self.ligne)]
        random.shuffle(
            positions
        )  # Pour que les entités s’activent dans un ordre aléatoire

        for x, y in positions:
            entite = self.lire_case(x, y)
            # Si la case n’est pas vide et que l’entité a une méthode agir, on l'appelle
            if entite is not None and hasattr(entite, "agir"):
                entite.agir(x, y, self)

        self.__chronon += 1  # Le temps avance

    # Affiche la grille dans le terminal
    def afficher(self):
        for y in range(self.ligne):
            ligne = ""
            for x in range(self.colonne):
                entite = self.lire_case(x, y)
                if entite is None:
                    ligne += "."  # case vide
                elif entite.__class__.__name__.lower() == "poisson":
                    ligne += "P"
                elif entite.__class__.__name__.lower() == "requin":
                    ligne += "R"
                else:
                    ligne += "?"  # autre (pas encore prévu)
            print(ligne)
        print("Chronon :", self.__chronon)
        print()


def test():
    # Création du monde et initialisation
    monde = Monde(colonne=20, ligne=10)
    monde.initialiser(
        nb_poissons=10, nb_requins=5, classe_poisson=Poisson, classe_requin=Requin
    )

    # Exécution de quelques tours de simulation
    for _ in range(10):
        monde.afficher()
        monde.executer_chronon()


if __name__ == "__main__":
    test()
