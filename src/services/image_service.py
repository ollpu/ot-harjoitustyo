import PIL.Image
from entities.image import Image

class ImageService:
    def __init__(self, image_opener=PIL.Image.open):
        self.image_opener = image_opener

    def load_from_file(self, file):
        """
        Load any image from given path and resize it to be suitable for the UI.

        Args:
            file: Path to the image file.
        Returns:
            An Image entity.
        """

        return Image.load_from_file(file, self.image_opener)

default_image_service = ImageService()
