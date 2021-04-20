import unittest
from image import Image, IMAGE_SIZE

class PILImageMock:
    def __init__(self, size, filename, resized=False):
        self.size = size
        self._filename = filename
        self._resized = resized

    def resize(self, new_size):
        assert isinstance(new_size[0], int)
        assert isinstance(new_size[1], int)
        return PILImageMock(new_size, self._filename, True)

    def was_resized(self):
        return self._resized


class TestImage(unittest.TestCase):
    def test_load_image_from_file_performs_resize(self):
        image = Image.load_from_file("filename.png",
                                     opener=lambda f: PILImageMock((520, 300), f))
        assert image.loaded_image.was_resized()
        self.assertEqual(image.loaded_image.size, (IMAGE_SIZE, 575*IMAGE_SIZE//1000))

    def test_load_image_from_file_not_resized_when_suitable(self):
        image = Image.load_from_file("filename.png",
                                     opener=lambda f: PILImageMock((IMAGE_SIZE, IMAGE_SIZE), f))
        assert not image.loaded_image.was_resized()
