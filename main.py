from CLASSES.Monde import Monde
from CLASSES.Grille import Grille
from CLASSES.Poisson import Poisson
from CLASSES.Requin import Requin
from graphique import bo_graphique
from time import sleep
from os import system, name as system_name
from parametres import CLEAR_TERMINAL, TEMPS_RAFRAICHISSEMENT, CHRONON_MAX, NOMBRE_INITIAUX_POISSON, NOMBRE_INITIAUX_REQUIN


def main() -> None:
    """
    Lancement de la simulation Wa-Tor (auteurs: Sanae, Romain et César)
    Cette fonction initialise le monde, affiche l'état initial et exécute les chronons de la simulation.
    Elle rafraîchit l'affichage du terminal à chaque itération et gère le temps d'attente entre les étapes de la simulation.
    La simulation s'arrête après 10 chronons.

    Returns:
        None
    """
    # Rafraichir le terminal (cls pour windows et clear pour linux)
    system("cls" if system_name == "nt" else "clear")

    # Initialisation de Wa-Tor
    monde_wa_tor = Monde()
    monde_wa_tor.initialiser()
    monde_wa_tor.afficher()
    sleep(TEMPS_RAFRAICHISSEMENT)

    # Ecoulement du temps
    compteur = 0
    nbr_cases = monde_wa_tor.colonnes * monde_wa_tor.lignes
    liste_nombre_poissons = [NOMBRE_INITIAUX_POISSON]
    liste_nombre_requins = [NOMBRE_INITIAUX_REQUIN]
    liste_nombre_cases_vides = [nbr_cases - NOMBRE_INITIAUX_POISSON - NOMBRE_INITIAUX_REQUIN]
    liste_chronons = [0]
    while True:
        # Rafraichir le terminal (cls pour windows et clear pour linux)
        # if CLEAR_TERMINAL:
        #     system("cls" if system_name == "nt" else "clear")

        monde_wa_tor.executer_chronon()
        monde_wa_tor.afficher()
        # sleep(TEMPS_RAFRAICHISSEMENT)




        if monde_wa_tor.chronon % 5 == 0:

        #partie graphique
            liste_chronons.append(monde_wa_tor.chronon)

            nbr_poisson = monde_wa_tor.grille.nombre_entite(Poisson)
            liste_nombre_poissons.append(nbr_poisson)

            nbr_requin = monde_wa_tor.grille.nombre_entite(Requin)
            liste_nombre_requins.append(nbr_requin)

            nbr_cases_vides = nbr_cases - nbr_poisson - nbr_requin
            liste_nombre_cases_vides.append(nbr_cases_vides)

            dict_entite = {'poisson': liste_nombre_poissons, 'requin': liste_nombre_requins, 'cases vides': liste_nombre_cases_vides}
        



        compteur += 1
        if compteur >= CHRONON_MAX:
            bo_graphique(liste_chronons, dict_entite)
            break


main()
