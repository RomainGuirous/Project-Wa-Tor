from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE

class Grille:
    def __init__(self, colonnes: int = NOMBRE_COLONNE_GRILLE, lignes: int = NOMBRE_LIGNE_GRILLE) -> None:
        self.colonnes = colonnes
        self.lignes = lignes
        self.grille = self.liste_grille_vide()

    def liste_grille_vide(self) -> list[list]:
        liste_resultat = []
        for y in range(self.lignes):
            ligne = []
            for x in range(self.colonnes):
                ligne.append(None)
            liste_resultat.append(ligne)
        return liste_resultat

    def lire_case(self, position_tuple: tuple[int, int]) -> any:
        x = position_tuple[0] % self.lignes
        y = position_tuple[1] % self.colonnes
        return self.grille[x][y]

    def placer_entite(self, position_tuple: tuple[int, int], entite: object) -> None:
        x = position_tuple[0] % self.lignes
        y = position_tuple[1] % self.colonnes
        self.grille[x][y] = entite

    def cases_voisines(self, position_tuple: tuple[int, int]) -> list[tuple[int, int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        liste_voisins = []
        for x_direction, y_direction in directions:
            x = (position_tuple[0] + x_direction) % self.colonnes
            y = (position_tuple[1] + y_direction) % self.lignes
            liste_voisins.append((x, y))
        return liste_voisins
    
    def cases_libres(self, position_tuple: tuple[int, int]):
        liste_cases_libres = []
        liste_cases_voisines = self.cases_voisines(position_tuple)
        for case in liste_cases_voisines:
            if self.lire_case(case) == None:
                liste_cases_libres.append(case)
        return liste_cases_libres


grille_demo = Grille(5,5)
grille_demo.placer_entite((2,3),"P")
grille_demo.placer_entite((4,3),"P")
print(grille_demo.cases_libres((3,3)))