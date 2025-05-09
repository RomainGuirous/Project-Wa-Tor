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
        toutes_les_positions = [
            (x, y) for x in range(self.colonnes) for y in range(self.lignes)
        ]
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

            if entite.age >= TEMPS_REPRODUCTION_POISSON:
                bebe = entite.se_reproduire()
                self.grille.placer_entite(*ancienne_position, bebe)
                entite._age = 0

            entite.se_deplacer()
            nouvelle_position = entite.position

            if self.grille.lire_case(*nouvelle_position) is None:
                self.grille.placer_entite(*nouvelle_position, entite)
                self.grille.placer_entite(*ancienne_position, None)

        self.chronon += 1

#fonction executer toutes les actions
def executer_toutes_les_actions(self):
    #Liste de toutes les positions de la grille
    toutes_les_positions = []
    for col in range(self.colonnes):
        for lig in range(self.lignes):
            toutes_les_positions.append((col, lig))

    #Mélange pour l’ordre aléatoire
    random.shuffle(toutes_les_positions)

    deja_agis = [] #pour éviter que nos entités agissent 2 fois dans un même tour

    #Étape 1 : les REQUINS agissent
    for position in toutes_les_positions:
        entite = self.grille.lire_case(*position)

        if entite is None:
            continue
        if entite.__class__.__name__.lower() != "requin":
            continue
        if position in deja_agis:
            continue

        voisins = self.grille.voisins(*position)

        #Trouver les cases vides autour
        cases_vides = []
        for voisin in voisins:
            if self.grille.lire_case(*voisin) is None:
                cases_vides.append(voisin)

        #Trouver les poissons autour
        cases_poissons = []
        for voisin in voisins:
            voisin_entite = self.grille.lire_case(*voisin)
            if voisin_entite is not None and voisin_entite.__class__.__name__.lower() == "poisson":
                cases_poissons.append(voisin)

        #Si au moins une case vide
        if len(cases_vides) > 0:
            # Requin se reproduit on place reproduction en priorité
            if entite.age % entite.age_reproduction == 0:
                bebe = entite.se_reproduire()
                self.grille.placer_entite(*position, bebe)

            #Sinon, s’il peut manger un poisson
            elif len(cases_poissons) > 0:
                cible = random.choice(cases_poissons)
                self.grille.placer_entite(*cible, entite)
                self.grille.placer_entite(*position, None)
                entite.position = cible
                entite.gagner_energie()
                deja_agis.append(cible)
                continue  # Requin a agi, on passe

            # Sinon, déplacement simple
            else:
                nouvelle_position = random.choice(cases_vides)
                self.grille.placer_entite(*nouvelle_position, entite)
                self.grille.placer_entite(*position, None)
                entite.position = nouvelle_position
                deja_agis.append(nouvelle_position)

    #Étape 2 mtn c'est les POISSONS agissent
    random.shuffle(toutes_les_positions)

    for position in toutes_les_positions:
        entite = self.grille.lire_case(*position)

        if entite is None:
            continue
        if entite.__class__.__name__.lower() != "poisson":
            continue
        if position in deja_agis:
            continue

        voisins = self.grille.voisins(*position)

        #Trouver les cases vides
        cases_vides = []
        for voisin in voisins:
            if self.grille.lire_case(*voisin) is None:
                cases_vides.append(voisin)

        if len(cases_vides) > 0:
            #Poisson se reproduit
            if entite.age % entite.age_reproduction == 0:
                bebe = entite.se_reproduire()
                self.grille.placer_entite(*position, bebe)
            else:
                nouvelle_position = random.choice(cases_vides)
                self.grille.placer_entite(*nouvelle_position, entite)
                self.grille.placer_entite(*position, None)
                entite.position = nouvelle_position
                deja_agis.append(nouvelle_position)
#fin de ma fonction executer toutes les actions



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
