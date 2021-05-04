from entities.game import Game
from entities.round import Round
from repositories.game_repository import default_game_repository

from default_game import load_test_game

class GameService:
    def __init__(self, repo=default_game_repository, test_game_factory=load_test_game):
        self._repository = repo
        self._test_game_factory = test_game_factory

    def new_game(self, name):
        return Game(name, [])

    def add_round(self, game, pairs):
        game.rounds.append(Round(pairs))

    def save_game(self, game):
        self._repository.store(game)

    def remove_game(self, game):
        self._repository.remove(game)

    def get_all_games(self):
        return self._repository.all()

    def load_test_game_if_empty(self):
        if len(self._repository.all()) == 0:
            self._repository.store(self._test_game_factory())

default_game_service = GameService()
