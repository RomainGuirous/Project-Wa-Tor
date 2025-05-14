# /!\ RAJOUTER NOUVEAUX PARAMETRES DANS LE FICHIER parametres.py.exemple /!\

# paramètres de la simulation
# ---------------------------

# grille
CHRONON_MAX = 50
NOMBRE_LIGNE_GRILLE = 7
NOMBRE_COLONNE_GRILLE = 7

# poisson
NOMBRE_INITIAUX_POISSON = 10
LIMITE_AGE_POISSON = 20
TEMPS_GESTION_POISSON = 6

# requin
NOMBRE_INITIAUX_REQUIN = 2
LIMITE_AGE_REQUIN = 50
AGE_ADULTE_REQUIN = 10
TEMPS_GESTION_REQUIN = 10
ENERGIE_INITIALE_REQUIN = 10
ENERGIE_MAX_REQUIN = 15
ENERGIE_FAIM_REQUIN = 10
ENERGIE_FAIM_CRITIQUE_REQUIN = 3
GAIN_ENERGIE_EN_MANGEANT_POISSON = 4
PERTE_ENERGIE_EN_COMBATTANT = 2

# rocher
TAILLE_REFUGE = 4
TAILLE_ENTREE_REFUGE = 2

# paramètres d'affichage
# ----------------------
# Affichage dynamique ?
# True: ne voir que la dernière carte
# False: conserver l'affichage de toutes les cartes
CLEAR_TERMINAL = True

# Intervalle d'affichage
INTERVALLE_AFFICHAGE = 5

# Temps de rafraichissement du terminal en secondes
TEMPS_RAFRAICHISSEMENT = 2

if __name__ == "__main__":
    # Code à exécuter uniquement si ce fichier est lancé directement
    print("Ce fichier est conçu pour être importé, pas exécuté directement.")
