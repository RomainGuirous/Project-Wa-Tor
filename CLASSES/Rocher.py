import random

random.seed()
from parametres import TAILLE_REFUGE, TAILLE_ENTREE_REFUGE


class Rocher:
    def __str__(self) -> str:
        """Représentation humainement lisible.

        Returns:
            str: description de self
        """
        return "Juste un rocher..."


def positions_de_la_cavite(
    position_depart: tuple[int, int] = (0, 0),
    taille: int = TAILLE_REFUGE,
    taille_entree: int = TAILLE_ENTREE_REFUGE,
) -> list[tuple[int, int]]:
    """Retourne une liste de positions sur la grille pour dessiner
    une cavité carré de rochers d'une taille donnée avec une entrée
    positionnée aléatoirement avec une taille donnée.

    Args:
        position_depart (tuple[int, int], optional): Position du coin premier coin de la grille. Defaults to (0,0)
        taille (int, optional): Taille de la cavité. Defaults to TAILLE_REFUGE.
        taille_entree (int, optional): Taille de l'entrée de la cavité. Defaults to TAILLE_ENTREE_REFUGE.

    Returns:
        list[tuple[int, int]]: Liste des positions des rochers pour former la cavité sur la grille.
    """

    liste_positions_rochers = []
    position = list(position_depart)
    for _ in range(taille):
        liste_positions_rochers.append(tuple(position))
        position[0] += 1
    for _ in range(taille):
        liste_positions_rochers.append(tuple(position))
        position[1] += 1
    for _ in range(taille):
        liste_positions_rochers.append(tuple(position))
        position[0] -= 1
    for _ in range(taille):
        liste_positions_rochers.append(tuple(position))
        position[1] -= 1

    position_entree = random.choice(liste_positions_rochers)
    index_position_entree = liste_positions_rochers.index(position_entree)
    for _ in range(taille_entree):
        liste_positions_rochers.pop(
            index_position_entree
            if index_position_entree <= len(liste_positions_rochers)
            else 0
        )

    return liste_positions_rochers
