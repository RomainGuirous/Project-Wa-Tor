from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE

class Grille:

    def __init__(self, nombre_ligne: int = NOMBRE_LIGNE_GRILLE, nombre_colonne: int = NOMBRE_COLONNE_GRILLE) -> list[list]:
        self.nombre_ligne = nombre_ligne
        self.nombre_colonne = nombre_colonne

    def liste_grille():

        grille = []
        for ligne in range(NOMBRE_LIGNE_GRILLE):
            ligne = []
            for colonne in range(NOMBRE_COLONNE_GRILLE):
                ligne.append(" ")
            grille.append(ligne)

        return grille