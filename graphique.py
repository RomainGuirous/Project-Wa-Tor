import matplotlib

matplotlib.use("TkAgg")  # Utilise le backend TkAgg

import matplotlib.pyplot as plt


def graphique_populations(
    liste_abscisse: list[int], dico_entite: dict[str, list[int]]
) -> None:
    """
    Affiche un graphique représentant la population de chaque entité au fil du temps.

    Args:
        liste_abscisse (list[int]): Liste des chronons.
        dico_entite (dict[str, list[int]]): Dictionnaire contenant les populations de chaque entité.

    Returns:
        None: Crée un graphique et l'affiche.
    """
    fig, ax = plt.subplots()
    ax.stackplot(liste_abscisse, dico_entite.values(), labels=dico_entite.keys())
    ax.legend(loc="upper left", reverse=True)
    ax.set_title("Population Wa-Tor")
    ax.set_xlabel("Chronons")
    ax.set_ylabel("Nombre d'entités")

    plt.show()


if __name__ == "__main__":
    # Code à exécuter uniquement si ce fichier est lancé directement
    print("Ce fichier est conçu pour être importé, pas exécuté directement.")
