import pygame
import copy
import os
import cv2
import numpy as np
import parametres
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from graphique import graphique_populations
from parametres import (
    CHRONON_MAX,
    NOMBRE_LIGNE_GRILLE_PYGAME,
    NOMBRE_COLONNE_GRILLE_PYGAME,
    NOMBRE_INITIAUX_POISSON,
    NOMBRE_INITIAUX_REQUIN,
    NOMBRE_INITIAUX_SUPER_POISSON,
)

from CLASSES.Monde import Monde
from CLASSES.Poisson import Poisson, SuperPoisson
from CLASSES.Requin import Requin
from CLASSES.Rocher import Rocher

# Configuration espace
TAILLE_CASE = 20
LARGEUR = NOMBRE_COLONNE_GRILLE_PYGAME * TAILLE_CASE
HAUTEUR = NOMBRE_LIGNE_GRILLE_PYGAME * TAILLE_CASE
FPS = 1

# Initialisation
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("peripherique_pygame/son.mp3")
pygame.mixer.music.play(-1)
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Wa-Tor Simulation")
horloge = pygame.time.Clock()

# Aspect
police = pygame.font.SysFont("segoeui", 26, bold=True)
petite_police = pygame.font.SysFont("segoeui", 20, bold=False)


# Image
def charger_image(nom):
    """
    Charge une image et la redimensionne à la taille de la case.

    Args:
        nom (str): Le nom de l'image à charger.

    Returns:
        pygame.Surface: L'image chargée et redimensionnée.
    """
    chemin = os.path.join("peripherique_pygame", nom)
    return pygame.transform.scale(pygame.image.load(chemin), (TAILLE_CASE, TAILLE_CASE))


IMG_POISSON_SPECIAL = charger_image("poisson_special.png")
IMG_POISSON = charger_image("poisson.png")
IMG_REQUIN = charger_image("requin.png")
IMG_ROCHER = charger_image("rocher.png")


# Menu
def dessiner_bouton(rect, texte, survol):
    """
    Dessine un bouton avec un texte au centre.

    Args:
        rect (pygame.Rect): Le rectangle du bouton.
        texte (str): Le texte à afficher sur le bouton.
        survol (bool): Indique si la souris survole le bouton.

    Returns:
        None
    """
    couleur = (90, 120, 180, 190) if survol else (60, 70, 100, 180)
    btn_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    btn_surf.fill(couleur)
    ecran.blit(btn_surf, rect.topleft)
    pygame.draw.rect(ecran, (220, 220, 255), rect, 2, border_radius=12)
    label = police.render(texte, True, (240, 240, 250))
    ecran.blit(
        label,
        (
            rect.x + (rect.width - label.get_width()) // 2,
            rect.y + (rect.height - label.get_height()) // 2,
        ),
    )


def afficher_menu():
    """
    Affiche le menu principal (début de lancement) de la simulation.
    Permet de choisir le nombre de poissons, requins et poissons spéciaux.

    Returns:
        None
    """
    video = cv2.VideoCapture("peripherique_pygame/video_fond.mp4")
    nb_poissons = NOMBRE_INITIAUX_POISSON
    nb_requins = NOMBRE_INITIAUX_REQUIN
    nb_super_poissons = NOMBRE_INITIAUX_SUPER_POISSON
    btn_lancer = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 100, 200, 50)
    btn_quitter = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 170, 200, 50)
    moins_poisson = pygame.Rect(LARGEUR // 2 - 150, HAUTEUR // 2 - 30, 40, 40)
    plus_poisson = pygame.Rect(LARGEUR // 2 + 110, HAUTEUR // 2 - 30, 40, 40)
    moins_requin = pygame.Rect(LARGEUR // 2 - 150, HAUTEUR // 2 + 30, 40, 40)
    plus_requin = pygame.Rect(LARGEUR // 2 + 110, HAUTEUR // 2 + 30, 40, 40)
    moins_poisson_speciaux = pygame.Rect(LARGEUR // 2 - 150, HAUTEUR // 2 - 90, 40, 40)
    plus_poisson_speciaux = pygame.Rect(LARGEUR // 2 + 110, HAUTEUR // 2 - 90, 40, 40)

    en_menu = True
    while en_menu:
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame = cv2.resize(frame, (LARGEUR, HAUTEUR))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        surface = pygame.surfarray.make_surface(frame)
        ecran.blit(surface, (0, 0))
        titre = police.render("Wa-Tor Simulation", True, (240, 240, 250))
        ecran.blit(titre, (LARGEUR // 2 - titre.get_width() // 2, 40))

        souris = pygame.mouse.get_pos()
        ecran.blit(
            police.render(f"Poissons : {nb_poissons}", True, (240, 240, 250)),
            (LARGEUR // 2 - 100, HAUTEUR // 2 - 30),
        )
        dessiner_bouton(moins_poisson, "-", moins_poisson.collidepoint(souris))
        dessiner_bouton(plus_poisson, "+", plus_poisson.collidepoint(souris))

        ecran.blit(
            police.render(f"Requins : {nb_requins}", True, (240, 240, 250)),
            (LARGEUR // 2 - 100, HAUTEUR // 2 + 30),
        )
        dessiner_bouton(moins_requin, "-", moins_requin.collidepoint(souris))
        dessiner_bouton(plus_requin, "+", plus_requin.collidepoint(souris))

        ecran.blit(
            police.render(f"Poissons + : {nb_super_poissons}", True, (240, 240, 250)),
            (LARGEUR // 2 - 100, HAUTEUR // 2 - 80),
        )
        dessiner_bouton(
            moins_poisson_speciaux, "-", moins_poisson_speciaux.collidepoint(souris)
        )
        dessiner_bouton(
            plus_poisson_speciaux, "+", plus_poisson_speciaux.collidepoint(souris)
        )

        dessiner_bouton(btn_lancer, "Lancer", btn_lancer.collidepoint(souris))
        dessiner_bouton(btn_quitter, "Quitter", btn_quitter.collidepoint(souris))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video.release()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if moins_poisson.collidepoint(souris):
                    nb_poissons = max(0, nb_poissons - 1)
                if plus_poisson.collidepoint(souris):
                    nb_poissons = min(100, nb_poissons + 1)
                if moins_requin.collidepoint(souris):
                    nb_requins = max(0, nb_requins - 1)
                if plus_requin.collidepoint(souris):
                    nb_requins = min(100, nb_requins + 1)
                if moins_poisson_speciaux.collidepoint(souris):
                    nb_super_poissons = max(0, nb_super_poissons - 1)
                if plus_poisson_speciaux.collidepoint(souris):
                    nb_super_poissons = min(100, nb_super_poissons + 1)
                if btn_lancer.collidepoint(souris):
                    setattr(parametres, "NOMBRE_INITIAUX_POISSON", nb_poissons)
                    setattr(parametres, "NOMBRE_INITIAUX_REQUIN", nb_requins)
                    setattr(
                        parametres, "NOMBRE_INITIAUX_SUPER_POISSON", nb_super_poissons
                    )
                    en_menu = False
                if btn_quitter.collidepoint(souris):
                    video.release()
                    pygame.quit()
                    exit()

        pygame.display.flip()
        pygame.event.pump()
        horloge.tick(30)
    video.release()


# Mini-graphe en temps réel
def dessiner_courbe_mini(poissons_speciaux, poissons, requins):
    """
    Dessine un mini-graphe en bas à droite de l'écran.

    Args:
        poissons_speciaux (list): Liste des poissons spéciaux.
        poissons (list): Liste des poissons.
        requins (list): Liste des requins.

    Returns:
        None
    """
    fig = Figure(figsize=(3.5, 1.2), dpi=100)
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.plot(poissons_speciaux, color="orange", linewidth=1, label="Poissons spéciaux")
    ax.plot(poissons, color="yellow", linewidth=1, label="Poissons")
    ax.plot(requins, color="blue", linewidth=1, label="Requins")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor("#0F121E")
    fig.patch.set_alpha(0)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()
    size = canvas.get_width_height()
    surf = pygame.image.frombuffer(raw_data, size, "RGBA")
    ecran.blit(surf, (LARGEUR - size[0] - 10, HAUTEUR - size[1] - 10))


# Grille
def afficher_grille(monde, poissons_speciaux, poissons, requins):
    """
    Affiche la grille du monde avec les entités présentes.

    Args:
        monde (Monde): Instance du monde à afficher.
        poissons_speciaux (list): Liste des poissons spéciaux.
        poissons (list): Liste des poissons.
        requins (list): Liste des requins.

    Returns:
        None
    """
    ecran.fill((15, 18, 30))
    for y in range(NOMBRE_LIGNE_GRILLE_PYGAME):
        for x in range(NOMBRE_COLONNE_GRILLE_PYGAME):
            pos = (x, y)
            entite = monde.grille.lire_case(pos)
            if isinstance(entite, SuperPoisson):
                ecran.blit(IMG_POISSON_SPECIAL, (x * TAILLE_CASE, y * TAILLE_CASE))
            elif isinstance(entite, Poisson):
                ecran.blit(IMG_POISSON, (x * TAILLE_CASE, y * TAILLE_CASE))
            elif isinstance(entite, Requin):
                ecran.blit(IMG_REQUIN, (x * TAILLE_CASE, y * TAILLE_CASE))
            elif isinstance(entite, Rocher):
                ecran.blit(IMG_ROCHER, (x * TAILLE_CASE, y * TAILLE_CASE))
    dessiner_courbe_mini(poissons_speciaux, poissons, requins)


# Fin avec affichage ecran & possibilité de relancer le jeu
def afficher_ecran_fin():
    """
    Affiche l'écran de fin de simulation avec un fond vidéo et des boutons pour rejouer ou quitter.
    Permet de relancer la simulation ou de quitter le programme.

    Returns:
        None"""
    video = cv2.VideoCapture("peripherique_pygame/video_fond.mp4")
    btn_rejouer = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 - 30, 200, 50)
    btn_quitter = pygame.Rect(LARGEUR // 2 - 100, HAUTEUR // 2 + 40, 200, 50)
    while True:
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        frame = cv2.resize(frame, (LARGEUR, HAUTEUR))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        fond = pygame.surfarray.make_surface(frame)
        ecran.blit(fond, (0, 0))

        label = police.render("Simulation terminée", True, (240, 240, 250))
        ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, HAUTEUR // 4))
        souris = pygame.mouse.get_pos()
        dessiner_bouton(btn_rejouer, "Rejouer", btn_rejouer.collidepoint(souris))
        dessiner_bouton(btn_quitter, "Quitter", btn_quitter.collidepoint(souris))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video.release()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_rejouer.collidepoint(souris):
                    video.release()
                    afficher_menu()
                    simulation()
                    return
                elif btn_quitter.collidepoint(souris):
                    video.release()
                    pygame.quit()
                    exit()
        pygame.display.flip()
        horloge.tick(30)


# Simulation
def simulation():
    """
    Fonction principale de la simulation.
    Elle gère l'affichage de la grille, le déroulement des tours, la pause et l'alerte d'extinction.
    Elle affiche également un graphique des populations d'entités au fil du temps.

    Returns:
        None
    """
    monde = Monde()
    monde.initialiser()
    tour = 0
    mondes_enregistres = []
    index_tour_affiche = -1  # -1 = en temps réel
    pause = False
    historique_poissons_speciaux = []
    historique_poissons = []
    historique_requins = []
    btn_pause = pygame.Rect(LARGEUR - 130, 10, 120, 40)
    while tour < CHRONON_MAX:
        horloge.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    index_tour_affiche = -1  # Retour au temps réel

                elif pause and event.key == pygame.K_LEFT:
                    if index_tour_affiche == -1:
                        index_tour_affiche = len(mondes_enregistres) - 2
                    elif index_tour_affiche > 0:
                        index_tour_affiche -= 1

                elif pause and event.key == pygame.K_RIGHT:
                    if (
                        index_tour_affiche != -1
                        and index_tour_affiche < len(mondes_enregistres) - 1
                    ):
                        index_tour_affiche += 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_pause.collidepoint(pygame.mouse.get_pos()):
                    pause = not pause
                    index_tour_affiche = -1

        if not pause:
            monde.executer_chronon()
            mondes_enregistres.append(copy.deepcopy(monde))
            if len(mondes_enregistres) > 3:
                mondes_enregistres.pop(0)

            tour += 1
            nb_super_poissons = monde.grille.nombre_espece(SuperPoisson)
            nb_poissons = monde.grille.nombre_espece(Poisson)
            nb_requins = monde.grille.nombre_espece(Requin)
            historique_poissons.append(nb_poissons)
            historique_requins.append(nb_requins)
            historique_poissons_speciaux.append(nb_super_poissons)

            # ALERTE EXTINCTION
            if nb_poissons == 0 or nb_requins == 0 or nb_super_poissons == 0:
                pygame.mixer.music.stop()  # Stoppe la musique de fond

                if nb_super_poissons == 0:
                    espece_morte = "Poissons spéciaux"
                elif nb_poissons == 0:
                    espece_morte = "Poissons"
                else:
                    espece_morte = "Requins"

                pygame.display.set_caption(f"EXTINCTION : {espece_morte}")
                alarme = pygame.mixer.Sound("peripherique_pygame/alarme.mp3")
                alarme.play()

                ecran.fill((150, 0, 0))
                alerte = police.render("EXTINCTION !", True, (255, 255, 255))
                ecran.blit(
                    alerte, (LARGEUR // 2 - alerte.get_width() // 2, HAUTEUR // 2 - 20)
                )

                pygame.display.flip()
                pygame.time.wait(
                    11000
                )  # Attendre 11 secondes (le son continue pendant ce temps)
                alarme.stop()
                pygame.mixer.music.play(-1)  # Relance la musique en boucle

                # Affichage du graphique à la fin
                liste_chronons = list(range(len(historique_poissons)))
                dico_entite = {
                    "Poissons": historique_poissons,
                    "Requins": historique_requins,
                    "Poissons spéciaux": historique_poissons_speciaux,
                }
                graphique_populations(liste_chronons, dico_entite)
                afficher_ecran_fin()  # Revenir directement à l'écran de fin
                return

        # Affichage du bon état en fonction du mode (pause ou temps réel)
        if pause and index_tour_affiche != -1:
            monde_a_afficher = mondes_enregistres[index_tour_affiche]
            afficher_grille(
                monde_a_afficher,
                historique_poissons,
                historique_requins,
                historique_poissons_speciaux,
            )

            # Calcul du numéro de tour affiché
            tour_affiche = tour - (len(mondes_enregistres) - 1 - index_tour_affiche)

            # Compter le nombre d'entités à ce moment-là
            nb_super_poissons_affiche = monde_a_afficher.grille.nombre_espece(
                SuperPoisson
            )
            nb_poissons_affiche = monde_a_afficher.grille.nombre_espece(Poisson)
            nb_requins_affiche = monde_a_afficher.grille.nombre_espece(Requin)

            # Mise à jour du titre de la fenêtre
            pygame.display.set_caption(
                f"Wa-Tor (Tour {tour_affiche}) | Super poisson : {nb_super_poissons_affiche} | Poisson : {nb_poissons_affiche} | Requin : {nb_requins_affiche}"
            )
        else:
            afficher_grille(
                monde,
                historique_poissons,
                historique_requins,
                historique_poissons_speciaux,
            )
            pygame.display.set_caption(
                f"Wa-Tor (Tour {tour}) | Super poisson : {nb_super_poissons} | Poisson : {nb_poissons} | Requin : {nb_requins}"
            )

        # Affichage de "PAUSE" en grand au centre
        if pause:
            overlay = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 100))
            ecran.blit(overlay, (0, 0))
            texte_pause = police.render("PAUSE", True, (255, 255, 255))
            ecran.blit(
                texte_pause,
                (
                    LARGEUR // 2 - texte_pause.get_width() // 2,
                    HAUTEUR // 2 - texte_pause.get_height() // 2,
                ),
            )
        pygame.display.flip()
    afficher_ecran_fin()


# Lancement
afficher_menu()
simulation()
pygame.mixer.music.stop()
