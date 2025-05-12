import matplotlib
matplotlib.use('TkAgg')  # Utilise le backend TkAgg

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

def bo_graphique(liste_abscisse, dico_entite):
    # Data from United Nations World Population Prospects (Revision 2019)


    fig, ax = plt.subplots()
    ax.stackplot(liste_abscisse, dico_entite.values())
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Population Wa-Tor')
    ax.set_xlabel('Chronons')
    ax.set_ylabel("Nombre d'entités (milliards)")
    # add tick at every 200 million people
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(.2))

    plt.show()