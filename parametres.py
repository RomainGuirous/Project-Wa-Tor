# paramètres de la simulation
# ---------------------------

# grille
CHRONON_MAX = 400
NOMBRE_LIGNE_GRILLE = 15
NOMBRE_COLONNE_GRILLE = 10

# poisson
NOMBRE_INITIAUX_POISSON = 130
LIMITE_AGE_POISSON = 10
TEMPS_GESTION_POISSON = 2

# requin
NOMBRE_INITIAUX_REQUIN = 10
LIMITE_AGE_REQUIN = 11
TEMPS_GESTION_REQUIN = 5
ENERGIE_INITIALE_REQUIN = 4
ENERGIE_MAX_REQUIN = 4
ENERGIE_FAIM_REQUIN = 6
GAIN_ENERGIE_EN_MANGEANT_POISSON = 2

# paramètres d'affichage
# ----------------------
# Affichage dynamique ?
# True: ne voir que la dernière carte
# False: conserver l'affichage de toutes les cartes
CLEAR_TERMINAL = True

# Intervalle d'affichage
INTERVALLE_AFFICHAGE = 5

# Temps de rafraichissement du terminal en secondes
TEMPS_RAFRAICHISSEMENT = 0.5

if __name__ == "__main__":
    # Code à exécuter uniquement si ce fichier est lancé directement
    print("Ce fichier est conçu pour être importé, pas exécuté directement.")
