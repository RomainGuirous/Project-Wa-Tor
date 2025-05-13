from rich.emoji import Emoji

def symbole_case_vide() -> str:
    """Symbole pour les cases vides.

    Returns:
        str: Emoji sélectionné
    """
    # symbole = Emoji.replace(":water_wave:")  # case vide 🌊
    symbole = Emoji.replace(":blue_square:")  # case vide 🟦
    # symbole = Emoji.replace(":black_large_square:")  # case vide ⬛
    # symbole = Emoji.replace(":blue_circle:")  # case vide 🔵
    # symbole = Emoji.replace(":droplet:")  # case vide 💧
    # symbole = Emoji.replace(":large_blue_diamond:")  # case vide 🔷
    # symbole = Emoji.replace(":sweat_droplets:")  # case vide 💦
    return symbole

def symbole_poisson() -> str:
    """Symbole pour les poissons.

    Returns:
        str: Emoji sélectionné
    """
    # symbole = Emoji.replace(":fish:") # poisson 🐟
    symbole = Emoji.replace(":tropical_fish:") # poisson tropical 🐠
    # symbole = Emoji.replace(":blowfish:") # poisson ballon 🐡
    return symbole

def symbole_requin() -> str:
    """Symbole pour les requins.

    Returns:
        str: Emoji sélectionné    
    """
    symbole = Emoji.replace(":shark:") # requin 🦈
    return symbole

def symbole_inconnu() -> str:
    """Symbole pour les entités inconnues

    Returns:
        str: Emoji sélectionné
    """
    symbole = Emoji.replace(":grey_question:") # point d'interrogation ❔
    # symbole = Emoji.replace(":white_question_mark:") #point d'interrogation ❔
    return symbole


# Autres symboles disponibles qui pourraient être utiles pour le projet Wa-Tor:
# Emoji.replace(":boat:")  # bateau ⛵
# Emoji.replace(":speedboat:")  # bateau 🚤
# Emoji.replace(":crab:")  # crabe 🦀
# Emoji.replace(":diving_mask:")  # plongeur 🤿
# Emoji.replace(":dolphin:")  # dauphin 🐬
# Emoji.replace(":flipper:")  # dauphin 🐬
# Emoji.replace(":ice:")  # iceberg 🧊
# Emoji.replace(":lobster:")  # iceberg 🦞
# Emoji.replace(":white_circle:")  # rocher ⚪
# Emoji.replace(":whale:")  # baleine 🐳
# Emoji.replace(":whale:")  # baleine 🐋
# Emoji.replace(":turtle:")  # tortue 🐢
# Emoji.replace(":surfer:")  # surfer 🏄
# Emoji.replace(":shrimp:")  # crevette 🦐
# Emoji.replace(":rowboat:")  # canoe 🚣
# Emoji.replace(":octopus:")  # pieuvre 🐙
# Emoji.replace(":microbe:")  # microbe 🦠
# Emoji.replace(":mermaid:")  # sirène 🧜‍
# Emoji.replace(":black_square_button:") # rocher 🔲
# Emoji.replace(":white_large_square_button:") # rocher ⬜

if __name__ == "__main__":
    # Code à exécuter uniquement si ce fichier est lancé directement
    print("Ce fichier est conçu pour être importé, pas exécuté directement.")