import random
random.seed()
from parametres import TAILLE_REFUGE, TAILLE_ENTREE_REFUGE

class Rocher:
    def __str__():
        print("Juste un rocher...")


def positions_de_la_cavite(position_depart: tuple[int, int], taille: int = TAILLE_REFUGE, taille_entree: int = TAILLE_ENTREE_REFUGE):

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
        liste_positions_rochers.pop(index_position_entree if index_position_entree <= len(liste_positions_rochers) else 0)

    return liste_positions_rochers



