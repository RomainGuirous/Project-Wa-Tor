class Grille:
    def __init__(self, colonnes, lignes):
        self.colonnes = colonnes
        self.lignes = lignes
        self.grille = self.liste_grille_vide()

    def liste_grille_vide(self):
        liste_resultat = []
        for y in range(self.lignes):
            ligne = []
            for x in range(self.colonnes):
                ligne.append(None)
            liste_resultat.append(ligne)
        return liste_resultat

    def lire_case(self, x, y):
        x = x % self.colonnes
        y = y % self.lignes
        return self.grille[y][x]

    def placer_entite(self, x, y, entite):
        x = x % self.colonnes
        y = y % self.lignes
        self.grille[y][x] = entite

    def voisins(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        liste_voisins = []
        for dx, dy in directions:
            nx = (x + dx) % self.colonnes
            ny = (y + dy) % self.lignes
            liste_voisins.append((nx, ny))
        return liste_voisins

Grille_demo = Grille(5,5)
print(Grille_demo.liste_grille_vide())