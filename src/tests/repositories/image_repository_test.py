import unittest
from tests.test_database import database_connection

from repositories.image_repository import ImageRepository
from entities.image import Image

class ImageStub:
    def __init__(self, data):
        self.id = None
        self.data = data

    @staticmethod
    def load_from_bytes(data):
        return ImageStub(data)

    def as_png_bytes(self):
        return self.data

class TestImageRepository(unittest.TestCase):
    def setUp(self):
        self.repository = ImageRepository(database_connection, ImageStub)
        self.repository.clear()

    def test_ensure_stored_sets_id(self):
        image = ImageStub(b"[kissa]")
        self.repository.ensure_stored(image)
        assert image.id is not None

    def test_get_retrieves_original_data_after_clear_cache(self):
        image = ImageStub(b"[kissa]")
        image_id = self.repository.ensure_stored(image)
        self.repository.clear_cache()
        loaded_image = self.repository.get_lazy(image_id)
        assert loaded_image.data == b"[kissa]"
