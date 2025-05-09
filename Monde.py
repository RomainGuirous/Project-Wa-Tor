import os
import time
import random  # Pour utiliser le mélange aléatoire des positions
from rich.emoji import Emoji
from Grille import Grille
from Poisson import Poisson
from Requin import Requin
from parametres import (
    NOMBRE_LIGNE_GRILLE,
    NOMBRE_COLONNE_GRILLE,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_REQUIN,
    TEMPS_REPRODUCTION_POISSON,
)

random.seed()


# Classe qui représente le monde Wa-Tor
class Monde:
    def __init__(self):
        self.grille = Grille(NOMBRE_COLONNE_GRILLE, NOMBRE_LIGNE_GRILLE)
        self.chronon = 0
        self.colonnes = NOMBRE_COLONNE_GRILLE
        self.lignes = NOMBRE_LIGNE_GRILLE

    def initialiser(self, nb_poissons, nb_requins, classe_poisson, classe_requin):
        toutes_les_positions = [
            (x, y) for x in range(self.colonnes) for y in range(self.lignes)
        ]
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
        """Execution de la phase dynamique associée à 1 chronon"""

        # Incrément du chronon
        self.chronon += 1

        # Obtenir une liste aléatoires de toutes les positions dans la grille
        toutes_les_positions = [
            (x, y) for x in range(self.colonnes) for y in range(self.lignes)
        ]

        # Parcourir les entités et éxecuter les effets du temps
        for x, y in toutes_les_positions:
            entite = self.grille.lire_case(x, y)
            if entite == None:
                continue

            # Effet du temps qui passe
            entite.vieillir()
            if isinstance(entite, Requin):
                entite.perte_d_energie()
            entite.mourir()

            # Nettoyage. Note:
            # cela empechera les requins de manger des poissons morts
            # cela permettra aux autres entites de se déplacer sur les case occupés par les entités mortes
            self.grille.nettoyer_case(x, y)

        self.executer_toutes_les_actions()

        # Parcourir les entités pour nettoyer les morts
        for x, y in toutes_les_positions:
            entite = self.grille.lire_case(x, y)
            if entite is None:
                continue

            # Nettoyage
            self.grille.nettoyer_case(x, y)

    # TODO: Sanae implemente cette partie
    def executer_toutes_les_actions(self):
        pass
        # # Obtenir une liste aléatoires de toutes les positions dans la grille
        # toutes_les_positions = [
        #     (x, y) for x in range(self.colonnes) for y in range(self.lignes)
        # ]
        # random.shuffle(toutes_les_positions)

        # # Parcourir aléatoirement les entités et éxecuter leurs actions
        # for x, y in toutes_les_positions:
        #     entite = self.grille.lire_case(x, y)
        #     if entite is None:
        #         continue

        #     ancienne_position = entite.position
        #     if entite.age >= TEMPS_REPRODUCTION_POISSON:
        #         bebe = entite.se_reproduire()
        #         self.grille.placer_entite(*ancienne_position, bebe)
        #         entite._age = 0

        #     entite.se_deplacer()
        #     nouvelle_position = entite.position

        #     if self.grille.lire_case(*nouvelle_position) is None:
        #         self.grille.placer_entite(*nouvelle_position, entite)
        #         self.grille.placer_entite(*ancienne_position, None)

    def afficher(self):
        for y in range(self.lignes):
            ligne_separateur = "+"
            ligne = "|"
            for x in range(self.colonnes):
                entite = self.grille.lire_case(x, y)
                if entite is None:
                    # ligne += Emoji.replace(":water_wave:")  # case vide 🌊
                    ligne += Emoji.replace(":blue_square:")  # case vide 🟦
                    # ligne += Emoji.replace(":black_large_square:")  # case vide ⬛
                    # ligne += Emoji.replace(":blue_circle:")  # case vide 🔵
                    # ligne += Emoji.replace(":droplet:")  # case vide 💧
                    # ligne += Emoji.replace(":large_blue_diamond:")  # case vide 🔷
                    # ligne += Emoji.replace(":sweat_droplets:")  # case vide 💦
                elif entite.__class__.__name__.lower() == "poisson":
                    # ligne += Emoji.replace(":fish:") # poisson 🐟
                    ligne += Emoji.replace(":tropical_fish:")  # poisson tropical 🐠
                    # ligne += Emoji.replace(":blowfish:") # poisson ballon 🐡
                elif entite.__class__.__name__.lower() == "requin":
                    ligne += Emoji.replace(":shark:")  # requin 🦈
                else:
                    ligne += Emoji.replace(
                        ":grey_question:"
                    )  # point d'interrogation ❔
                    # ligne += Emoji.replace(":white_question_mark:") #point d'interrogation ❔
                    # ligne += Emoji.replace(":boat:")  # bateau ⛵
                    # ligne += Emoji.replace(":speedboat:")  # bateau 🚤
                    # ligne += Emoji.replace(":crab:")  # crabe 🦀
                    # ligne += Emoji.replace(":diving_mask:")  # plongeur 🤿
                    # ligne += Emoji.replace(":dolphin:")  # dauphin 🐬
                    # ligne += Emoji.replace(":flipper:")  # dauphin 🐬
                    # ligne += Emoji.replace(":ice:")  # iceberg 🧊
                    # ligne += Emoji.replace(":lobster:")  # iceberg 🦞
                    # ligne += Emoji.replace(":white_circle:")  # rocher ⚪
                    # ligne += Emoji.replace(":whale:")  # baleine 🐳
                    # ligne += Emoji.replace(":whale:")  # baleine 🐋
                    # ligne += Emoji.replace(":turtle:")  # tortue 🐢
                    # ligne += Emoji.replace(":surfer:")  # surfer 🏄
                    # ligne += Emoji.replace(":shrimp:")  # crevette 🦐
                    # ligne += Emoji.replace(":rowboat:")  # canoe 🚣
                    # ligne += Emoji.replace(":octopus:")  # pieuvre 🐙
                    # ligne += Emoji.replace(":microbe:")  # microbe 🦠
                    # ligne += Emoji.replace(":mermaid:")  # sirène 🧜‍
                    # ligne += Emoji.replace(":black_square_button:") # rocher 🔲
                    # ligne += Emoji.replace(":white_large_square_button:") # rocher ⬜

                ligne_separateur += "--+"
                ligne += "|"

            if y == 0:
                print("+--------------+")
                print("| WA-TOR WORLD |")
                print("+--------------+\n")
                print(f"Chronon: {self.chronon}\n")

            print(ligne_separateur)
            print(ligne)
        else:
            print(ligne_separateur)


def test():
    # Création du monde et initialisation
    monde = Monde()
    monde.initialiser(
        nb_poissons=NOMBRE_INITIAUX_POISSON,
        nb_requins=NOMBRE_INITIAUX_REQUIN,
        classe_poisson=Poisson,
        classe_requin=Requin,
    )

    for _ in range(10):
        # Rafraichir le terminal (cls pour windows et clear pour linux)
        os.system("cls" if os.name == "nt" else "clear")

        # Affichage de la grille (avec en-tete)
        monde.afficher()
        monde.executer_chronon()

        # Attendre 2 sec
        time.sleep(2)


if __name__ == "__main__":
    test()
