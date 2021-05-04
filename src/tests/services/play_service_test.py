import random
import unittest

from services.play_service import PlayService, GuessResult
from entities.game import Game
from entities.round import Round

class TestPlayService(unittest.TestCase):
    def setUp(self):
        seeded_random = random.Random(12)
        self.service = PlayService(shuffle=seeded_random.shuffle)
        round1 = Round([("Koira", "[koira]"), ("Kissa", "[kissa]")])
        round2 = Round([("Pöytä", "[pöytä]")])
        self.game = Game("Peli", [round1, round2])

    def test_start_game_provides_text_and_images(self):
        self.service.start_game(self.game)
        text = self.service.get_text()
        assert text in ["Koira", "Kissa"]
        images = self.service.get_images()
        assert len(images) == 2
        assert ("[koira]", 0) in images
        assert ("[kissa]", 1) in images
        used_images = self.service.get_used_images()
        assert used_images == [False, False]

    def test_guess_correct_then_continue_round(self):
        self.service.start_game(self.game)
        text = self.service.get_text()
        assert text == "Kissa"
        response = self.service.submit_guess(1)
        assert response == GuessResult.CORRECT_ONE

    def test_guess_incorrect(self):
        self.service.start_game(self.game)
        text = self.service.get_text()
        assert text == "Kissa"
        response = self.service.submit_guess(0)
        assert response == GuessResult.INCORRECT

    def test_guess_correct_updates_used_images(self):
        self.service.start_game(self.game)
        self.service.submit_guess(1)
        used_images = self.service.get_used_images()
        assert used_images == [False, True]

    def test_guess_incorrect_does_not_update_used_images(self):
        self.service.start_game(self.game)
        self.service.submit_guess(0)
        used_images = self.service.get_used_images()
        assert used_images == [False, False]

    def test_guess_end_round(self):
        self.service.start_game(self.game)
        self.service.submit_guess(1)
        response = self.service.submit_guess(0)
        assert response == GuessResult.CORRECT_ROUND_COMPLETE

    def test_start_new_round_provides_text_and_images(self):
        self.service.start_game(self.game)
        assert self.service.next_round()
        text = self.service.get_text()
        assert text == "Pöytä"
        images = self.service.get_images()
        assert images == [("[pöytä]", 0)]
        used_images = self.service.get_used_images()
        assert used_images == [False]

    def test_trying_to_start_new_round_past_last_resets(self):
        self.service.start_game(self.game)
        self.service.next_round()
        assert not self.service.next_round()
        assert self.service.get_text() is None
