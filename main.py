from Monde import Monde
from parametres import NOMBRE_INITIAUX_POISSON, NOMBRE_INITIAUX_REQUIN
from Poisson import Poisson
from Requin import Requin
from time import sleep
from os import system, name as system_name


def main():
    """Lancement de la simulation Wa-Tor (auteurs: Sanae, Romain et César)"""

    # Rafraichir le terminal (cls pour windows et clear pour linux)
    system("cls" if system_name == "nt" else "clear")

    # Initialisation de Wa-Tor
    monde_wa_tor = Monde()
    monde_wa_tor.initialiser(
        nb_poissons=NOMBRE_INITIAUX_POISSON,
        nb_requins=NOMBRE_INITIAUX_REQUIN,
        classe_poisson=Poisson,
        classe_requin=Requin,
    )
    monde_wa_tor.afficher()

    # Ecoulement du temps
    compteur = 0
    while True:
        # Rafraichir le terminal (cls pour windows et clear pour linux)
        system("cls" if system_name == "nt" else "clear")

        monde_wa_tor.executer_chronon()
        monde_wa_tor.afficher()
        sleep(2)

        compteur += 1
        if compteur >= 10:
            break


main()
