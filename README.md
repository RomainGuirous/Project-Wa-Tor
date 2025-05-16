# Project-Wa-Tor

## Description

**Project-Wa-Tor** est une simulation inspirée du modèle Wa-Tor, où poissons, super-poissons et requins évoluent dans un environnement en grille. Chaque entité suit des règles de micro-comportements simples communes ou dépendantes de son espèce (déplacement, reproduction, vieillissement, prédation, gestion de l’énergie, défense de territoire et fuite). Le projet propose :
- Un affichage terminal de la grille embelli d'emojis
- Une visualisation graphique de l’évolution des populations (Matplotlib),
- Une interface graphique interactive avec PyGame.

---

## Fonctionnalités

- Simulation d’un écosystème dynamique avec poissons et requins sur une grille toroidale
- Gestion du déplacement aléatoire, de la reproduction périodique, du vieillissement et autre effet du temps pour toutes les espèces.
- Gestion de l'alimentation (prédation) et de la défense du territoire (combat) des requins.
- Gestion de la fuite (déplacement anticipée), spécifique des super-poissons.
- Intégration d'une zone entourée de rochers connectée au reste du monde par une unique entrée.
- Affichage dynamique de la grille en temps réel dans le terminal.
- Visualisation graphique de l’évolution des populations (poissons, super-poissons, requins, cases vides) avec Matplotlib.
- Animation de l’évolution des populations avec `FuncAnimation`.
- Interface graphique interactive avec PyGame (sprites, boutons, menus).
- Multiples paramètres de configuration de la simulation via le fichier `parametres.py` couvrant les comportements des espèces, l'état initial du monde et les paramètres d'affichage.

---

## Structure du projet

### Fichiers principaux

- **`main.py`** : Point d’entrée de la simulation avec affichage terminale et visualisation graphique (Matplotlib).
- **`main_pygame.py`** : Version alternative avec interface graphique PyGame.
- **`parametres.py`** : Paramètres globaux de la simulation (effectifs, âges, énergie, options d’affichage, etc.).
- **`gestionnaire.py`** : Permet de gérer les différents actions des différentes entités et la mise à jour de la grille en conséquence.
- **`graphique.py`** : Affichage graphique et animation de l’évolution des populations avec Matplotlib.
- **`tools.py`** : Fonctions utilitaires (ex : rafraîchissement du terminal).

### Dossier `CLASSES`

- **`EtreVivant.py`** : Classe de base pour les entités vivantes (poissons, super-poissons, requins).
- **`Poisson.py`** : Classes Poisson et SuperPoisson, héritant de `EtreVivant`.
- **`Requin.py`** : Classe Requin, héritant de `EtreVivant`, avec intégration d'un niveau d’énergie et sa gestion.
- **`Grille.py`** : Classe Grille, gère la matrice du monde et les reconnaissances de voisinage.
- **`Monde.py`** : Classe Monde, orchestre la simulation, la grille et les entités.

### Dossier `peripherique_pygame`

- Contient les images utilisées pour l’interface graphique PyGame (`poisson.png`, `requin.png`, `rocher.png`, etc.).

---

## Prérequis, installation et mode d'emploi

- Python 3.10 ou supérieur.
- Installez les dépendances avec :
  ```bash
  pip install -r requirements.txt
- Configuration de votre simulation avant éxecution :
copiez-collez le fichier `parametres.py.exemple` en `parametres.py` et complétez les différents paramètres à vos propres valeurs pour tester différents scénarios
---

## Paramètres optimaux

- Ces paramètres font en sorte de faire durer la simulation pendant de longs cycles.

```py
# paramètres de la simulation
# ---------------------------

# grille
CHRONON_MAX = 1000000
NOMBRE_LIGNE_GRILLE = 20
NOMBRE_COLONNE_GRILLE = 40

# grille spécifique à Pygame
NOMBRE_LIGNE_GRILLE_PYGAME = 40
NOMBRE_COLONNE_GRILLE_PYGAME = 80
# NOMBRE_LIGNE_GRILLE = NOMBRE_LIGNE_GRILLE_PYGAME
# NOMBRE_COLONNE_GRILLE = NOMBRE_COLONNE_GRILLE_PYGAME

# poisson
NOMBRE_INITIAUX_POISSON = 0
NOMBRE_INITIAUX_SUPER_POISSON = 50
LIMITE_AGE_POISSON = 10
TEMPS_GESTION_POISSON = 2

# requin
NOMBRE_INITIAUX_REQUIN = 10
LIMITE_AGE_REQUIN = 35
AGE_ADULTE_REQUIN = 10
TEMPS_GESTION_REQUIN = 10
ENERGIE_INITIALE_REQUIN = 10
ENERGIE_MAX_REQUIN = 15
ENERGIE_FAIM_REQUIN = 10
ENERGIE_FAIM_CRITIQUE_REQUIN = 3
GAIN_ENERGIE_EN_MANGEANT_POISSON = 4
PERTE_ENERGIE_EN_COMBATTANT = 3

# être vivant
AFFICHER_COULEUR_AGE = True

# rocher
INCLURE_REFUGE = True
NOMBRE_REFUGES = 3
TAILLE_REFUGE = 6
TAILLE_ENTREE_REFUGE = 2

# paramètres d'affichage
# ----------------------
# Activer l'affichage terminal ?
AFFICHAGE_TERMINAL = False

# Affichage dynamique ?
# True: ne voir que la dernière carte
# False: conserver l'affichage de toutes les cartes
CLEAR_TERMINAL = True

# Intervalle d'affichage
INTERVALLE_AFFICHAGE = 5

# Temps de rafraichissement du terminal en secondes
TEMPS_RAFRAICHISSEMENT = 0.05

if __name__ == "__main__":
  # Code à exécuter uniquement si ce fichier est lancé directement
  print("Ce fichier est conçu pour être importé, pas exécuté directement.")
```

## Auteur.e.s
- Sanae Al Massati (code de la simulation, Pygame)
- Romain Guirous (code de la simulation, Matplotlib)
- César Gattano (code de la simulation, affichage terminal)

Le code de la simulation a été programmée en étroites interactions entre ces 3 personnes de manière agile et à contributions égales.
