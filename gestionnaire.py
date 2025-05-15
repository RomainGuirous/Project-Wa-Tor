from CLASSES.Requin import Requin
from CLASSES.Poisson import Poisson
from CLASSES.Grille import Grille
from parametres import ENERGIE_FAIM_REQUIN, ENERGIE_FAIM_CRITIQUE_REQUIN
import random

random.seed()

#region se reproduire

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

#region s'alimenter

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

#region se deplacer

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

#region combat

def execute_combattre_requin(
    requin: Requin,
    position: tuple[int, int],
    cases_voisines_requins_adultes: list[tuple[int, int]],
    grille: Grille,
    deja_agis: list[tuple[int, int]],
) -> bool:

    if all(
        [
            not requin.est_bebe,
            ENERGIE_FAIM_CRITIQUE_REQUIN < requin.energie <= ENERGIE_FAIM_REQUIN,
        ]
    ):
        # Execution action
        position_adversaire = random.choice(cases_voisines_requins_adultes)
        adversaire = grille.lire_case(position_adversaire)
        est_victorieux = requin.combattre(
            adversaire
        )  # True: le requin a changé de position, False: l'adversaire a changé de position

        if est_victorieux:
            # Gestion de la grille
            grille.placer_entite(requin.position, requin)
            grille.placer_entite(position, None)

            # Mémoire des entités ayant agis durant ce chronon
            deja_agis.append(requin.position)
        else:
            # Gestion de la grille
            grille.placer_entite(adversaire.position, adversaire)
            grille.placer_entite(position_adversaire, None)

            # Mémoire des entités ayant agis durant ce chronon
            deja_agis.append(adversaire.position)

        return True
    else:
        return False


# region TEST
def test():
    # Test execute_se_deplacer_entite
    grille_demo = Grille(5, 5)
    poisson_demo = Poisson((2, 3))
    requin_demo = Requin((4, 3))
    deja_agis = []

    grille_demo.placer_entite((2, 3), poisson_demo)
    grille_demo.placer_entite((4, 3), requin_demo)

    for ligne in grille_demo.grille:
        print(ligne)
    print("Test déplacement poisson")
    print(
        execute_se_deplacer_entite(
            poisson_demo,
            poisson_demo.position,
            grille_demo.cases_voisines_libres(poisson_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print("Test déplacement requin")
    print(
        execute_se_deplacer_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_voisines_libres(requin_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)

    print("\n\n\n")

    # Test executer_se_reproduire_entite
    grille_demo = Grille(5, 5)
    poisson_demo = Poisson((2, 3))
    requin_demo = Requin((4, 3))
    deja_agis = []

    grille_demo.placer_entite((2, 3), poisson_demo)
    grille_demo.placer_entite((4, 3), requin_demo)

    for ligne in grille_demo.grille:
        print(ligne)
    print("Test reproduction poisson")
    poisson_demo._est_enceinte = True
    print(
        execute_se_reproduire_entite(
            poisson_demo,
            poisson_demo.position,
            grille_demo.cases_voisines_libres(poisson_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print("Test reproduction requin (échec attendu)")
    print(
        execute_se_reproduire_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_voisines_libres(requin_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    requin_demo._est_enceinte = True
    print("Test reproduction requin")
    print(
        execute_se_reproduire_entite(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_voisines_libres(requin_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)

    print("\n\n\n")

    # Test execute_s_alimenter_requin
    grille_demo = Grille(5, 5)
    requin_demo = Requin((1, 1))
    poisson_demo = Poisson((1, 2))
    deja_agis = []

    grille_demo.placer_entite(requin_demo.position, requin_demo)
    grille_demo.placer_entite(poisson_demo.position, poisson_demo)
    for ligne in grille_demo.grille:
        print(ligne)
    print("Test alimentation requin")
    print("Energie:", requin_demo.energie)
    print(
        execute_s_alimenter_requin(
            requin_demo,
            requin_demo.position,
            grille_demo.cases_voisines_entites(Poisson, requin_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print("Energie:", requin_demo.energie)

    print("\n\n\n")

    # Test executer_combattre_requin
    grille_demo = Grille(5, 5)
    combattant1_demo = Requin((1, 1))
    combattant2_demo = Requin((1, 2))
    deja_agis = []

    grille_demo.placer_entite(combattant1_demo.position, combattant1_demo)
    grille_demo.placer_entite(combattant2_demo.position, combattant2_demo)
    for ligne in grille_demo.grille:
        print(ligne)
    print("Test combat requin")
    print("Energie:", combattant1_demo.energie, combattant2_demo.energie)
    print("est_vivant:", combattant1_demo.est_vivant, combattant2_demo.est_vivant)
    print(
        execute_combattre_requin(
            combattant1_demo,
            combattant1_demo.position,
            grille_demo.cases_voisines_entites(Requin, combattant1_demo.position),
            grille_demo,
            deja_agis,
        )
    )
    for ligne in grille_demo.grille:
        print(ligne)
    print("Energie:", combattant1_demo.energie, combattant2_demo.energie)
    print("est_vivant:", combattant1_demo.est_vivant, combattant2_demo.est_vivant)


if __name__ == "__main__":
    test()
