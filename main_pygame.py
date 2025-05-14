import pygame
import cv2
import numpy as np
import time
import parametres

# Import des paramètres de simulation depuis le fichier 'parametres.py'
from parametres import (
    CHRONON_MAX,
    NOMBRE_LIGNE_GRILLE,
    NOMBRE_COLONNE_GRILLE,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_REQUIN,
    AFFICHER_COULEUR_AGE,
)

# On importe les classes principales
from CLASSES.Monde import Monde
from CLASSES.Poisson import Poisson
from CLASSES.Requin import Requin

# Chargement et lecture de la musique de fond
pygame.mixer.init()
pygame.mixer.music.load("peripherique_pygame/son.mp3")
pygame.mixer.music.play(-1)  # Lecture en boucle

# Paramètres d’affichage (taille, couleurs, police…)
TAILLE_PIXEL = 4
FPS = 20  # Nombre de tours par seconde (1 = lent = visible)
LARGEUR = NOMBRE_COLONNE_GRILLE * TAILLE_PIXEL
HAUTEUR = NOMBRE_LIGNE_GRILLE * TAILLE_PIXEL

# Définition des couleurs (fond, poissons, requins, etc.)
COULEUR_FOND = (15, 18, 30)
COULEUR_VIDE = (100, 180, 255)
COULEUR_POISSON = (255, 255, 0)
COULEUR_REQUIN = (160, 160, 160)
COULEUR_TEXTE = (240, 240, 250)
COULEUR_SURVOL = (100, 150, 255)
# A améliorer : chagement couleur plus flash


COULEUR_BTN_BG = (60, 70, 100, 180)
# Initialisation de la fenêtre Pygame
pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Wa-Tor Simulation")
horloge = pygame.time.Clock()

# Polices d’écriture pour les textes
police = pygame.font.SysFont("segoeui", 26, bold=True)
petite_police = pygame.font.SysFont("segoeui", 20, bold=False)

# Vidéo de fond qui défile derrière la grille
video_simul = cv2.VideoCapture("peripherique_pygame/video_fond.mp4")


# Fonction pour afficher un bouton avec texte
def dessiner_bouton(rect, texte, survol):
    couleur = (90, 120, 180, 190) if survol else COULEUR_BTN_BG
    btn_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    btn_surf.fill(couleur)
    ecran.blit(btn_surf, rect.topleft)
    pygame.draw.rect(ecran, (220, 220, 255), rect, 2, border_radius=12)
    label = police.render(texte, True, COULEUR_TEXTE)
    ecran.blit(
        label,
        (
            rect.x + (rect.width - label.get_width()) // 2,
            rect.y + (rect.height - label.get_height()) // 2,
        ),
    )


# Menu de démarrage avant de lancer la simulation
def afficher_menu():
    video = cv2.VideoCapture("peripherique_pygame/video_fond.mp4")
    nb_poissons = NOMBRE_INITIAUX_POISSON
    nb_requins = NOMBRE_INITIAUX_REQUIN

    # Définition des boutons
    btn_lancer = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 100, 200, 50)
    btn_quitter = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 170, 200, 50)
    moins_poisson = pygame.Rect(LARGEUR // 2 - 150, HAUTEUR // 2 - 30, 40, 40)
    plus_poisson = pygame.Rect(LARGEUR // 2 + 110, HAUTEUR // 2 - 30, 40, 40)
    moins_requin = pygame.Rect(LARGEUR // 2 - 150, HAUTEUR // 2 + 30, 40, 40)
    plus_requin = pygame.Rect(LARGEUR // 2 + 110, HAUTEUR // 2 + 30, 40, 40)

    en_menu = True
    while en_menu:
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Affichage vidéo
        frame = cv2.resize(frame, (LARGEUR, HAUTEUR))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        surface = pygame.surfarray.make_surface(frame)
        ecran.blit(surface, (0, 0))

        # Titre aspect
        titre = police.render("Wa-Tor Simulation", True, COULEUR_TEXTE)
        ecran.blit(titre, (LARGEUR // 2 - titre.get_width() // 2, 40))

        # Interaction avec les boutons
        souris = pygame.mouse.get_pos()
        ecran.blit(
            police.render(f"Poissons : {nb_poissons}", True, COULEUR_TEXTE),
            (LARGEUR // 2 - 80, HAUTEUR // 2 - 30),
        )
        dessiner_bouton(moins_poisson, "-", moins_poisson.collidepoint(souris))
        dessiner_bouton(plus_poisson, "+", plus_poisson.collidepoint(souris))

        ecran.blit(
            police.render(f"Requins : {nb_requins}", True, COULEUR_TEXTE),
            (LARGEUR // 2 - 80, HAUTEUR // 2 + 30),
        )
        dessiner_bouton(moins_requin, "-", moins_requin.collidepoint(souris))
        dessiner_bouton(plus_requin, "+", plus_requin.collidepoint(souris))

        dessiner_bouton(btn_lancer, "Lancer", btn_lancer.collidepoint(souris))
        dessiner_bouton(btn_quitter, "Quitter", btn_quitter.collidepoint(souris))

        # Gestion des clics
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video.release()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if moins_poisson.collidepoint(souris):
                    nb_poissons = max(0, nb_poissons - 1)
                if plus_poisson.collidepoint(souris):
                    nb_poissons = min(100, nb_poissons + 1)
                if moins_requin.collidepoint(souris):
                    nb_requins = max(0, nb_requins - 1)
                if plus_requin.collidepoint(souris):
                    nb_requins = min(100, nb_requins + 1)
                if btn_lancer.collidepoint(souris):
                    # Mise à jour des valeurs dans les paramètres
                    setattr(parametres, "NOMBRE_INITIAUX_POISSONS", nb_poissons)
                    setattr(parametres, "NOMBRE_INITIAUX_REQUINS", nb_requins)
                    en_menu = False
                if btn_quitter.collidepoint(souris):
                    video.release()
                    pygame.quit()
                    exit()

        pygame.display.flip()
        pygame.event.pump()
        horloge.tick(30)
    video.release()


# Fonction principale pour dessiner la grille et les entités
def dessiner_monde(monde, tour, pause=False):
    ret, frame = video_simul.read()
    if not ret:
        video_simul.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = video_simul.read()
    frame = cv2.resize(frame, (LARGEUR, HAUTEUR))
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    fond = pygame.surfarray.make_surface(frame)
    ecran.blit(fond, (0, 0))

    # Dessin de la carte
    surface = np.zeros((NOMBRE_COLONNE_GRILLE, NOMBRE_LIGNE_GRILLE, 3), dtype=np.uint8)
    for y in range(NOMBRE_LIGNE_GRILLE):
        for x in range(NOMBRE_COLONNE_GRILLE):
            entite = monde.grille.lire_case((x, y))
            if isinstance(entite, Poisson):
                if AFFICHER_COULEUR_AGE:
                    age = min(getattr(entite, "_age", 0), 20)
                    surface[x, y] = (255, max(150, 255 - age * 5), max(0, 50 - age * 2))
                else:
                    surface[x, y] = COULEUR_POISSON
            elif isinstance(entite, Requin):
                if AFFICHER_COULEUR_AGE:
                    age = min(getattr(entite, "_age", 0), 20)
                    gris = max(60, 200 - age * 7)
                    surface[x, y] = (gris, gris, gris)
                else:
                    surface[x, y] = COULEUR_REQUIN
            else:
                surface[x, y] = COULEUR_VIDE

    surf = pygame.surfarray.make_surface(np.transpose(surface, (1, 0, 2)))
    zoom = pygame.transform.scale(surf, (LARGEUR, HAUTEUR))
    ecran.blit(zoom, (0, 0))

    ecran.blit(police.render(f"Tour : {tour}", True, (60, 100, 180)), (20, 10))
    if pause:
        ecran.blit(police.render("Pause", True, (255, 255, 100)), (LARGEUR - 160, 10))

    # Affichage de la légende en bas
    largeur_legende = 260
    hauteur_legende = 110
    fond_legende = pygame.Surface((largeur_legende, hauteur_legende), pygame.SRCALPHA)
    fond_legende.fill((0, 0, 0, 150))
    ecran.blit(fond_legende, (20, HAUTEUR - hauteur_legende - 20))

    titre_legende = petite_police.render(
        "Population (âge croissant)", True, (255, 255, 255)
    )
    ecran.blit(titre_legende, (30, HAUTEUR - hauteur_legende - 10 - 6))

    legendes = [
        ("Poisson", (255, 255, 0), (200, 100, 0)),
        ("Requin", (200, 200, 200), (60, 60, 60)),
    ]
    for i, (label, c1, c2) in enumerate(legendes):
        y = HAUTEUR - hauteur_legende + 20 + i * 30
        gradient = pygame.Surface((40, 15))
        for x in range(40):
            r = int(c1[0] + (c2[0] - c1[0]) * x / 39)
            g = int(c1[1] + (c2[1] - c1[1]) * x / 39)
            b = int(c1[2] + (c2[2] - c1[2]) * x / 39)
            pygame.draw.line(gradient, (r, g, b), (x, 0), (x, 15))
        ecran.blit(gradient, (30, y))
        txt = petite_police.render(label, True, (255, 255, 255))
        ecran.blit(txt, (75, y))


# Fonction qui fait tourner la simulation
def lancer_simulation():
    monde = Monde()
    monde.initialiser()
    tour = 0
    pause = False

    while tour < CHRONON_MAX:
        horloge.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
        if not pause:
            monde.executer_chronon()
            tour += 1
        dessiner_monde(monde, tour, pause)
        pygame.display.flip()
    afficher_ecran_fin()


# Affichage de fin
def afficher_ecran_fin():
    btn_rejouer = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 - 30, 200, 50)
    btn_quitter = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 40, 200, 50)
    while True:
        ecran.fill(COULEUR_FOND)
        label = police.render("Simulation terminée", True, COULEUR_TEXTE)
        ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, HAUTEUR // 4))
        souris = pygame.mouse.get_pos()
        dessiner_bouton(btn_rejouer, "Rejouer", btn_rejouer.collidepoint(souris))
        dessiner_bouton(btn_quitter, "Quitter", btn_quitter.collidepoint(souris))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_rejouer.collidepoint(souris):
                    afficher_menu()
                    lancer_simulation()
                    return
                if btn_quitter.collidepoint(souris):
                    pygame.quit()
                    exit()
        pygame.display.flip()
        horloge.tick(30)


# On lance le programme
afficher_menu()
lancer_simulation()
pygame.mixer.music.stop()
