import os
import time
import random  # Pour utiliser le mélange aléatoire des positions
from rich.emoji import Emoji
from Poisson import Poisson
from Requin import Requin
from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE, NOMBRE_INITIAUX_POISSON, NOMBRE_INITIAUX_REQUIN

random.seed()

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
            ligne_separateur = "+"
            ligne = "|"
            for x in range(self.colonne):
                entite = self.lire_case(x, y)
                if entite is None:
                    #ligne += Emoji.replace(":water_wave:")  # case vide 🌊
                    ligne += Emoji.replace(":blue_square:")  # case vide 🟦
                    #ligne += Emoji.replace(":black_large_square:")  # case vide ⬛
                    #ligne += Emoji.replace(":blue_circle:")  # case vide 🔵
                    #ligne += Emoji.replace(":droplet:")  # case vide 💧
                    #ligne += Emoji.replace(":large_blue_diamond:")  # case vide 🔷
                    #ligne += Emoji.replace(":sweat_droplets:")  # case vide 💦
                elif entite.__class__.__name__.lower() == "poisson":
                    #ligne += Emoji.replace(":fish:") # poisson 🐟
                    ligne += Emoji.replace(":tropical_fish:") # poisson tropical 🐠
                    #ligne += Emoji.replace(":blowfish:") # poisson ballon 🐡
                elif entite.__class__.__name__.lower() == "requin":
                    ligne += Emoji.replace(":shark:") # requin 🦈
                else:
                    ligne += Emoji.replace(":grey_question:") #point d'interrogation ❔
                    #ligne += Emoji.replace(":white_question_mark:") #point d'interrogation ❔
                    #ligne += Emoji.replace(":boat:")  # bateau ⛵
                    #ligne += Emoji.replace(":speedboat:")  # bateau 🚤
                    #ligne += Emoji.replace(":crab:")  # crabe 🦀
                    #ligne += Emoji.replace(":diving_mask:")  # plongeur 🤿
                    #ligne += Emoji.replace(":dolphin:")  # dauphin 🐬
                    #ligne += Emoji.replace(":flipper:")  # dauphin 🐬
                    #ligne += Emoji.replace(":ice:")  # iceberg 🧊
                    #ligne += Emoji.replace(":lobster:")  # iceberg 🦞
                    #ligne += Emoji.replace(":white_circle:")  # rocher ⚪
                    #ligne += Emoji.replace(":whale:")  # baleine 🐳
                    #ligne += Emoji.replace(":whale:")  # baleine 🐋
                    #ligne += Emoji.replace(":turtle:")  # tortue 🐢
                    #ligne += Emoji.replace(":surfer:")  # surfer 🏄
                    #ligne += Emoji.replace(":shrimp:")  # crevette 🦐
                    #ligne += Emoji.replace(":rowboat:")  # canoe 🚣
                    #ligne += Emoji.replace(":octopus:")  # pieuvre 🐙
                    #ligne += Emoji.replace(":microbe:")  # microbe 🦠
                    #ligne += Emoji.replace(":mermaid:")  # sirène 🧜‍
                    #ligne += Emoji.replace(":black_square_button:") # rocher 🔲
                    #ligne += Emoji.replace(":white_large_square_button:") # rocher ⬜

                ligne_separateur += "--+"
                ligne += "|"

            if y == 0:
                print("+--------------+", flush=True)
                print("| WA-TOR WORLD |", flush=True)
                print("+--------------+\n", flush=True)
                print(f"Chronon: {self.__chronon}\n")
                
            print(ligne_separateur, flush=True)
            print(ligne, flush=True)
        else:
            print(ligne_separateur, flush=True)



def test():
    # Création du monde et initialisation
    monde = Monde(colonne=NOMBRE_COLONNE_GRILLE, ligne=NOMBRE_LIGNE_GRILLE)
    monde.initialiser(
        nb_poissons=NOMBRE_INITIAUX_POISSON, nb_requins=NOMBRE_INITIAUX_REQUIN, classe_poisson=Poisson, classe_requin=Requin
    )

    # Exécution de quelques tours de simulation
    for _ in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')
        monde.afficher()
        monde.executer_chronon()
        time.sleep(2)



if __name__ == "__main__":
    test()
