from CLASSES.Monde import Monde
from time import sleep
from os import system, name as system_name
from parametres import CLEAR_TERMINAL


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
    sleep(2)

    # Ecoulement du temps
    compteur = 0
    while True:
        # Rafraichir le terminal (cls pour windows et clear pour linux)
        if CLEAR_TERMINAL:
            system("cls" if system_name == "nt" else "clear")

        monde_wa_tor.executer_chronon()
        monde_wa_tor.afficher()
        sleep(2)

        compteur += 1
        if compteur >= 10:
            break


main()
