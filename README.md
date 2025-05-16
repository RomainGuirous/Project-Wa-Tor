# Project-Wa-Tor

## Description

**Project-Wa-Tor** est une simulation inspirée du modèle Wa-Tor, où poissons, super-poissons et requins évoluent dans un environnement en grille. Chaque entité suit des règles de déplacement, reproduction, vieillissement, prédation et gestion de l’énergie. Le projet propose :
- Un affichage terminal de la grille,
- Une visualisation graphique de l’évolution des populations (Matplotlib),
- Une interface graphique interactive avec PyGame.

---

## Fonctionnalités

- Simulation d’un écosystème dynamique avec poissons, super-poissons et requins.
- Gestion de la reproduction, du vieillissement, du déplacement, de la prédation et de l’énergie.
- Affichage de la grille en temps réel dans le terminal.
- Visualisation graphique de l’évolution des populations (poissons, super-poissons, requins, cases vides) avec Matplotlib.
- Animation de l’évolution des populations avec `FuncAnimation`.
- Interface graphique interactive avec PyGame (sprites, boutons, menus).
- Paramétrage facile via le fichier `parametres.py`.

---

## Structure du projet

### Fichiers principaux

- **`main.py`** : Point d’entrée de la simulation terminale et graphique (Matplotlib).
- **`main_pygame.py`** : Version alternative avec interface graphique PyGame.
- **`parametres.py`** : Paramètres globaux de la simulation (effectifs, âges, énergie, options d’affichage, etc.).
- **`graphique.py`** : Affichage graphique et animation de l’évolution des populations avec Matplotlib.
- **`tools.py`** : Fonctions utilitaires (ex : rafraîchissement du terminal).

### Dossier `CLASSES`

- **`EtreVivant.py`** : Classe de base pour les entités vivantes (poissons, super-poissons, requins).
- **`Poisson.py`** : Classe Poisson et SuperPoisson, héritant de `EtreVivant`.
- **`Requin.py`** : Classe Requin, héritant de `EtreVivant`, avec gestion de l’énergie.
- **`Grille.py`** : Classe Grille, gère la matrice du monde et les interactions de voisinage.
- **`Monde.py`** : Classe Monde, orchestre la simulation, la grille et les entités.

### Dossier `peripherique_pygame`

- Contient les images utilisées pour l’interface graphique PyGame (`poisson.png`, `requin.png`, `rocher.png`, etc.).

---

## Prérequis

- Important :
Avant de lancer la simulation, transformez le fichier `parametres.py.exemple` en `parametres.py` et adaptez les paramètres à vos besoins
- Python 3.10 ou supérieur.
- Installez les dépendances avec :
  ```bash
  pip install -r requirements.txt