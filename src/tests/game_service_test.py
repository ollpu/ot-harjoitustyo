import sys
print(sys.path)
import unittest
from game_service import GameService, GuessResult
from game import Game
from round import Round

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.service = GameService()
        round1 = Round([("Koira", "[koira]"), ("Kissa", "[kissa]")])
        round2 = Round([("Pöytä", "[pöytä]")])
        self.game = Game([round1, round2])

    def test_start_game_provides_text_and_images(self):
        self.service.start_game(self.game)
        text = self.service.get_text()
        assert text in ["Koira", "Kissa"]
        images = self.service.get_images()
        assert len(images) == 2
        used_images = self.service.get_used_images()
        assert used_images == [False, False]
