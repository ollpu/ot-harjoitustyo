from entities.game import Game
from entities.round import Round
from repositories.game_repository import default_game_repository

from default_game import load_test_game

class GameService:
    def __init__(self, repo=default_game_repository, test_game_factory=load_test_game):
        """
        Construct a GameService.

        Args:
            repo: Game repository to use. `default_game_repository` by default.
            test_game_factory: Function that produces a test game. `default_game.load_test_game`
                               by default.
        """

        self._repository = repo
        self._test_game_factory = test_game_factory

    @staticmethod
    def new_game(name):
        """
        Create a new game.

        Args:
            name: The initial name of the game.
        Returns:
            New Game entity.
        """

        return Game(name, [])

    @staticmethod
    def add_round(game, pairs):
        """
        Add a round to a game.

        Args:
            game: Game to operate on.
            pairs: Pairs describing the new round.
        """

        game.rounds.append(Round(pairs))

    def save_game(self, game):
        """
        Store game in the repository.

        Args:
            game: Game to be stored.
        """

        self._repository.store(game)

    def remove_game(self, game):
        """
        Remove game from repository.

        Args:
            game: Game to be removed.
        """

        self._repository.remove(game)

    def get_all_games(self):
        """
        Get all games stored in the repository.

        Returns:
            An array of games.
        """

        return self._repository.all()

    def load_test_game_if_empty(self):
        """
        Load a test game if no games currently exists.
        """
        if len(self._repository.all()) == 0:
            self._repository.store(self._test_game_factory())

default_game_service = GameService()
