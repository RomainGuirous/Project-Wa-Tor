from CLASSES.Requin import Requin
from CLASSES.Poisson import Poisson
from CLASSES.Grille import Grille
from parametres import ENERGIE_FAIM_REQUIN
import random

random.seed()


def execute_se_reproduire_entite(
    entite: Requin | Poisson,
    position: tuple[int, int],
    cases_voisines_vides: list[tuple[int, int]],
    grille: Grille,
    deja_agis: list[tuple[int, int]],
) -> bool:

    if entite.est_enceinte:
        # Execution action
        bebe = entite.se_reproduire(
            cases_voisines_vides
        )  # L'entite a changé de position

        # Gestion de la grille
        grille.placer_entite(position, bebe)
        grille.placer_entite(entite.position, entite)

        # Mémoire des entités ayant agis durant ce chronon
        deja_agis.append(entite.position)
        return True
    else:
        return False


def execute_s_alimenter_requin(
    requin: Requin,
    position: tuple[int, int],
    cases_voisines_poissons: list[tuple[int, int]],
    grille: Grille,
    deja_agis: list[tuple[int, int]],
) -> bool:

    if len(cases_voisines_poissons) > 0 and requin.energie <= ENERGIE_FAIM_REQUIN:
        # Execution action
        cible = random.choice(cases_voisines_poissons)
        requin.s_alimenter(cible)  # Le requin a changé de position

        # Gestion de la grille
        grille.placer_entite(requin.position, requin)
        grille.placer_entite(position, None)

        # Mémoire des entités ayant agis durant ce chronon
        deja_agis.append(cible)
        return True
    else:
        return False


def execute_se_deplacer_entite(
    entite: Requin | Poisson,
    position: tuple[int, int],
    cases_voisines_vides: list[tuple[int, int]],
    grille: Grille,
    deja_agis: list[tuple[int, int]],
) -> bool:
    if len(cases_voisines_vides) > 0:
        # Execution action
        entite.se_deplacer(cases_voisines_vides)  # L'entité a changé de position

        # Gestion de la grille
        grille.placer_entite(entite.position, entite)
        grille.placer_entite(position, None)

        # Mémoire des entités ayant agis durant ce chronon
        deja_agis.append(entite.position)
        return True
    else:
        return False


# region TEST
def test():
    grille_demo = Grille(5, 5)
    poisson_demo = Poisson((2, 3))
    requin_demo = Requin((4, 3))
    deja_agis = []

    grille_demo.placer_entite((2, 3), poisson_demo)
    grille_demo.placer_entite((4, 3), requin_demo)

    for ligne in grille_demo.grille:
        print(ligne)
    print(
        execute_se_deplacer_entite(
            poisson_demo,
            poisson_demo.position,
            grille_demo.cases_libres(poisson_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print(
        execute_se_deplacer_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_libres(requin_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    poisson_demo._est_enceinte = True
    print(
        execute_se_reproduire_entite(
            poisson_demo,
            poisson_demo.position,
            grille_demo.cases_libres(poisson_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print(
        execute_se_reproduire_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_libres(_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    requin_demo._est_enceinte = True
    print(
        execute_se_reproduire_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_libres(_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)


if __name__ == "__main__":
    test()
