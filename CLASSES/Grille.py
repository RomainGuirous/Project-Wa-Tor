############################################################
# Pour permettre de lancer les tests...
#######################################
import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
############################################################
from parametres import NOMBRE_LIGNE_GRILLE, NOMBRE_COLONNE_GRILLE
from typing import Type  # cela correspond à un type classe


class Grille:
    def __init__(
        self, colonnes: int = NOMBRE_COLONNE_GRILLE, lignes: int = NOMBRE_LIGNE_GRILLE
    ) -> None:
        """Constructeur de la classe Grille.
        Initialise la grille avec le nombre de colonnes et de lignes spécifié.
        Args:
            colonnes (int): Nombre de colonnes de la grille.
            lignes (int): Nombre de lignes de la grille.
        """
        if colonnes <= 0 or lignes <= 0:
            raise ValueError(
                "Le nombre de colonnes et de lignes doit être supérieur à 0."
            )
        self.colonnes = colonnes
        self.lignes = lignes
        self.grille = self.liste_grille_vide()

    def liste_grille_vide(self) -> list[list]:
        """
        Crée une grille vide avec des cases initialisées à None.

        Returns:
            list[list]: Grille vide avec des cases initialisées à None.
        """
        liste_resultat = []
        for y in range(self.lignes):
            ligne = []
            for x in range(self.colonnes):
                ligne.append(None)
            liste_resultat.append(ligne)
        return liste_resultat

    def lire_case(self, position_tuple: tuple[int, int]) -> any:
        """
        Lit la valeur d'une case de la grille à une position donnée.

        Args:
            position_tuple (tuple[int, int]): Position de la case à lire.

        Returns:
            any: Valeur de la case à la position donnée.
        """
        x = position_tuple[0] % self.colonnes
        y = position_tuple[1] % self.lignes
        return self.grille[y][x]

    def nettoyer_case(self, position_tuple: tuple[int, int]) -> None:
        """
        Nettoie une case de la grille à une position donnée.
        Si l'entité à cette position n'est pas vivante, elle est supprimée de la grille.
        Si l'entité est vivante, elle reste dans la grille.

        Args:
            position_tuple (tuple[int, int]): Position de la case à nettoyer.

        Returns:
            None
        """
        entite = self.lire_case(position_tuple)
        if not entite.est_vivant:
            self.placer_entite(position_tuple, None)

    def placer_entite(self, position_tuple: tuple[int, int], entite: object) -> None:
        """
        Place une entité à une position donnée dans la grille.

        Args:
            position_tuple (tuple[int, int]): Position où placer l'entité.
            entite (object): L'entité à placer dans la grille.

        Returns:
            None
        """
        x = position_tuple[0] % self.colonnes
        y = position_tuple[1] % self.lignes
        self.grille[y][x] = entite

    def cases_voisines(self, position_tuple: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Renvoie la liste des cases voisines d'une case donnée.

        Args:
            position_tuple (tuple[int, int]): Position de la case dont on veut les voisines.

        Returns:
            list[tuple[int, int]]: Liste des positions des cases voisines.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        liste_voisins = set()
        for x_direction, y_direction in directions:
            x = (position_tuple[0] + x_direction) % self.colonnes
            y = (position_tuple[1] + y_direction) % self.lignes
            if (x, y) != position_tuple:
                liste_voisins.update([(x, y)])
        return list(liste_voisins)

    def cases_voisines_libres(
        self,
        position_tuple: tuple[int, int],
        positions_voisines: list[tuple[int, int]] = [],
    ):
        """
        Renvoie la liste des cases libres autour d'une case donnée.

        Args:
            position_tuple (tuple[int, int]): Position de la case dont on veut les cases libres.

        Returns:
            list[tuple[int, int]]: Liste des positions des cases libres.
        """
        if not positions_voisines:
            positions_voisines = self.cases_voisines(position_tuple)

        liste_cases_libres = [
            position_voisine
            for position_voisine in positions_voisines
            if self.lire_case(position_voisine) == None
        ]
        return liste_cases_libres

    def cases_voisines_entites(
        self,
        classe_entite,
        position_tuple: tuple[int, int],
        positions_voisines: list[tuple[int, int]] = [],
    ):
        """
        Renvoie la liste des cases libres autour d'une case donnée.

        Args:
            position_tuple (tuple[int, int]): Position de la case dont on veut les cases libres.

        Returns:
            list[tuple[int, int]]: Liste des positions des cases libres.
        """
        if not positions_voisines:
            positions_voisines = self.cases_voisines(position_tuple)

        liste_cases_poissons = [
            position_voisine
            for position_voisine in positions_voisines
            if isinstance(self.lire_case(position_voisine), classe_entite)
        ]
        return liste_cases_poissons

    def nombre_espece(self, espece: Type) -> int:
        nbr_espece = 0
        for x in range(self.colonnes):
            for y in range(self.lignes):
                if isinstance(self.lire_case((x, y)), espece):
                    nbr_espece += 1
        return nbr_espece


# region TEST
def test():
    grille_demo = Grille(5, 1)
    print("Cases voisines (monde 1D)")
    print(grille_demo.cases_voisines((2, 0)))

    grille_demo = Grille(5, 3)
    print("Cases voisines (monde 2D)")
    print(grille_demo.cases_voisines((2, 0)))

    grille_demo = Grille(5, 5)
    grille_demo.placer_entite((2, 3), "P")
    grille_demo.placer_entite((4, 3), "P")
    print("Cases voisines vides (monde 2D)")
    print(grille_demo.cases_voisines_libres((3, 3)))


if __name__ == "__main__":
    test()
