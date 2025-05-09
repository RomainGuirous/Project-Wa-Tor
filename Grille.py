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
    
    def nettoyer_case(self, x: int, y: int):
        """Remplace l'entite de la case par None si celle-ci
        est morte selon son paramètre est_vivant.

        Args:
            x (int): Première coordonnée
            y (int): Deuxième coordonnée
        """
        entite = self.lire_case(x, y)
        if not entite.est_vivant:
            self.placer_entite(x, y, None)

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