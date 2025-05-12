from os import system, name as system_name

def rafraichir_terminal() -> None:
    """Rafraichir le terminal"""
    # commande 'cls' sous windows
    # commande 'clear' sous unix
    system("cls" if system_name == "nt" else "clear")
    # Note 'nt' signifie 'new technology' pour identifier os Windows