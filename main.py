from CLASSES.Monde import Monde
from CLASSES.Poisson import Poisson, SuperPoisson
from CLASSES.Requin import Requin
from graphique import graphique_populations
from parametres import (
    CLEAR_TERMINAL,
    INTERVALLE_AFFICHAGE,
    CHRONON_MAX,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_SUPER_POISSON,
    NOMBRE_INITIAUX_REQUIN,
)
from tools import rafraichir_terminal


def main() -> None:
    """
    Lancement de la simulation Wa-Tor (auteurs: Sanae, Romain et César)
    Cette fonction initialise le monde, affiche l'état initial et exécute les chronons de la simulation.
    Elle rafraîchit l'affichage du terminal à chaque itération et gère le temps d'attente entre les étapes de la simulation.
    La simulation s'arrête après 10 chronons.
    Affichage graphique de la population de chaque entité au fil du temps.

    Returns:
        None
    """
    rafraichir_terminal()

    # Initialisation du monde Wa-Tor
    monde_wa_tor = Monde()
    monde_wa_tor.initialiser()
    monde_wa_tor.afficher()

    # Ecoulement du temps
    compteur = 0
    nbr_cases = monde_wa_tor.colonnes * monde_wa_tor.lignes
    nbr_poisson = NOMBRE_INITIAUX_POISSON
    liste_nombre_poissons = [NOMBRE_INITIAUX_POISSON]
    nbr_super_poisson = NOMBRE_INITIAUX_SUPER_POISSON
    liste_nombre_super_poissons = [NOMBRE_INITIAUX_SUPER_POISSON]
    nbr_requin = NOMBRE_INITIAUX_REQUIN
    liste_nombre_requins = [NOMBRE_INITIAUX_REQUIN]
    liste_nombre_cases_vides = [
        nbr_cases - NOMBRE_INITIAUX_POISSON - NOMBRE_INITIAUX_REQUIN
    ]
    liste_chronons = [0]
    while True:
        if CLEAR_TERMINAL:
            rafraichir_terminal()

        # Évolution du monde
        monde_wa_tor.executer_chronon()
        monde_wa_tor.afficher()

        # partie graphique
        if monde_wa_tor.chronon % INTERVALLE_AFFICHAGE == 0:

            liste_chronons.append(monde_wa_tor.chronon)

            nbr_super_poisson = monde_wa_tor.grille.nombre_espece(SuperPoisson)
            liste_nombre_super_poissons.append(nbr_super_poisson)

            nbr_poisson = monde_wa_tor.grille.nombre_espece(Poisson) - nbr_super_poisson
            liste_nombre_poissons.append(nbr_poisson)

            nbr_requin = monde_wa_tor.grille.nombre_espece(Requin)
            liste_nombre_requins.append(nbr_requin)

            nbr_cases_vides = nbr_cases - nbr_poisson - nbr_requin - nbr_super_poisson
            liste_nombre_cases_vides.append(nbr_cases_vides)

            dict_entite = {
                "poisson": liste_nombre_poissons,
                "super-poisson": liste_nombre_super_poissons,
                "requin": liste_nombre_requins,
                "cases vides": liste_nombre_cases_vides,
            }

        # Fin de la simulation
        compteur += 1
        if compteur >= CHRONON_MAX or nbr_requin <= 0:
            graphique_populations(liste_chronons, dict_entite)
            break


main()
