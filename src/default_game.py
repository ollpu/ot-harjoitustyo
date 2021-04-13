"""Load a hardcoded test game"""

from game import Game
from round import Round
from image import Image

def load_test_game():
    koira = Image.load_from_file("data/koira.jpg")
    kissa = Image.load_from_file("data/kissa.jpg")
    aurinko = Image.load_from_file("data/aurinko.jpg")
    return Game([
        Round([("Koira", koira), ("Kissa", kissa)]),
        Round([("Aurinko", aurinko)]),
    ])
