import unittest

from services.game_service import GameService
from entities.game import Game
from entities.round import Round

class GameRepositoryStub:
    def __init__(self):
        self._games = []
        self._next_id = 1

    def store(self, game):
        if game.id is None:
            game.id = self._next_id
            self._next_id += 1
            self._games.append(game)

    def remove(self, game):
        if game.id is not None:
            self._games.remove(game)
            game.id = None

    def all(self):
        return list(self._games)

    def clear(self):
        self._games = []

def test_game_factory():
    return Game("Testipeli", [
        Round([("Koira", "[Koira]"), ("Kissa", "[Kissa]")]),
        Round([("Aurinko", "[Aurinko]")]),
    ])

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_repository = GameRepositoryStub()
        self.service = GameService(self.game_repository, test_game_factory)

    def test_new_game_returns_empty_game(self):
        game = self.service.new_game("Empty game")
        self.assertEqual(game.name, "Empty game")
        self.assertEqual(game.rounds, [])

    def test_add_round_changes_game(self):
        game = Game("Empty game", [])
        self.service.add_round(game, [("Kameli", "[Kameli]"), ("Lepakko", "[Lepakko]")])
        self.assertEqual(game.rounds[0].pairs[1], ("Lepakko", "[Lepakko]"))

    def test_save_game_stores_game_in_repository(self):
        game = Game("Empty game", [("Kameli", "[Kameli]")])
        self.service.save_game(game)
        self.assertEqual(self.game_repository.all(), [game])

    def test_remove_game_removes_game_from_repository(self):
        game = Game("Empty game", [("Kameli", "[Kameli]")])
        self.game_repository.store(game)
        self.service.remove_game(game)
        self.assertEqual(self.game_repository.all(), [])

    def test_get_all_fetches_from_repository(self):
        game = Game("Empty game", [("Kameli", "[Kameli]")])
        self.game_repository.store(game)
        result = self.service.get_all_games()
        self.assertEqual(result, [game])

    def test_load_test_game_when_empty(self):
        self.service.load_test_game_if_empty()
        self.assertEqual(self.game_repository.all()[0].name, "Testipeli")

    def test_dont_load_test_game_when_not_empty(self):
        game = Game("Empty game", [("Kameli", "[Kameli]")])
        self.game_repository.store(game)
        self.service.load_test_game_if_empty()
        self.assertEqual(len(self.game_repository.all()), 1)
        self.assertEqual(self.game_repository.all()[0].name, "Empty game")
