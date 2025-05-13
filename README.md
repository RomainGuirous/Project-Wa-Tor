# Project-Wa-Tor

## Description
**Project-Wa-Tor** est une simulation basée sur le modèle de Wa-Tor, où des poissons et des requins évoluent dans un environnement simulé. Les entités interagissent entre elles selon des règles définies, comme la reproduction, le vieillissement, et la prédation. Le projet inclut également une visualisation graphique des populations au fil du temps.

## Fonctionnalités
- Simulation d'un écosystème avec des poissons et des requins.
- Gestion des comportements des entités :
  - Reproduction.
  - Vieillissement.
  - Déplacement.
  - Prédation (les requins mangent les poissons).
- Affichage dynamique de la grille dans le terminal.
- Visualisation graphique des populations avec Matplotlib.
- Animation des données en temps réel avec `FuncAnimation`.

## Structure du projet
Voici les principaux fichiers et leur rôle :

### Fichiers principaux
- **`main.py`** : Point d'entrée du programme. Gère la boucle principale de la simulation et collecte les données pour l'affichage graphique.
- **`parametres.py`** : Contient les paramètres globaux de la simulation (par exemple, nombre initial de poissons et de requins, limites d'âge, etc.).
- **`graphique.py`** : Gère l'affichage graphique des populations au fil du temps à l'aide de Matplotlib.
- **`README.md`** : Documentation du projet.

### Classes principales
- **`EtreVivant.py`** :
  - Classe de base pour les entités vivantes (poissons et requins).
  - Gère les comportements communs comme le vieillissement et la reproduction.
- **`Poisson.py`** :
  - Classe représentant les poissons.
  - Hérite de `EtreVivant`.
- **`Requin.py`** :
  - Classe représentant les requins.
  - Hérite de `EtreVivant`.
  - Ajoute des comportements spécifiques comme la gestion de l'énergie.
- **`Grille.py`** :
  - Classe représentant la grille où évoluent les entités.
  - Gère les positions des entités et les interactions entre elles.
- **`Monde.py`** :
  - Classe principale qui orchestre la simulation.
  - Gère la grille et les entités.

## Prérequis
- Python 3.10 ou supérieur.
- Bibliothèques Python :
  - `matplotlib`
  - `numpy` (si utilisé pour la gestion des matrices)
- Installez les dépendances avec :
  ```bash
  pip install -r requirements.txt