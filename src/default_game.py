
from entities.game import Game
from entities.round import Round
from entities.image import Image

def load_test_game():
    """
    Load a hardcoded test game

    Returns:
        A `Game`.
    """
    koira = Image.load_from_file("data/koira.jpg")
    kissa = Image.load_from_file("data/kissa.jpg")
    aurinko = Image.load_from_file("data/aurinko.jpg")
    return Game("Esimerkkipeli", [
        Round([("Koira", koira), ("Kissa", kissa)]),
        Round([("Aurinko", aurinko)]),
    ])
