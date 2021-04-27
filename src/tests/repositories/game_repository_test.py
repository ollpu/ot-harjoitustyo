import unittest
from repositories.game_repository import GameRepository
from tests.test_database import database_connection
from entities.game import Game
from entities.round import Round

class ImageRepositoryStub:
    def __init__(self):
        self._images = [None]

    def ensure_stored(self, image):
        for image_id, stored in enumerate(self._images):
            if stored == image:
                return image_id
        self._images.append(image)
        return len(self._images) - 1

    def get_lazy(self, image_id):
        assert image_id > 0
        return self._images[image_id]

class TestGameRepository(unittest.TestCase):
    def setUp(self):
        self.image_repo = ImageRepositoryStub()
        self.repository = GameRepository(database_connection, self.image_repo)
        self.repository.clear()
        round1 = Round([("Koira", "[koira]"), ("Kissa", "[kissa]")])
        round2 = Round([("Pöytä", "[pöytä]")])
        self.game = Game("Peli", [round1, round2])

    def test_storing_game_changes_listing(self):
        self.repository.store(self.game)
        assert self.repository.all()[0].rounds[0].pairs[1][0] == "Kissa"

    def test_clear_empties_listing(self):
        self.repository.store(self.game)
        self.repository.clear()
        assert len(self.repository.all()) == 0
