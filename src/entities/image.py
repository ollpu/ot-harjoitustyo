import io
import PIL.Image

IMAGE_SIZE = 200

class Image:
    """
    In-memory image abstraction, which stores a properly scaled version of an image.

    Attributes:
        id: Unique id used by the repository.
        loaded_image: PIL.Image
    """

    def __init__(self, image):
        """
        Construct an Image entity. ID is set to None initially.

        Args:
            image: A PIL image.
        """

        self.id = None
        self.loaded_image = image
        self._resize_if_necessary()

    @staticmethod
    def load_from_file(file, opener=PIL.Image.open):
        """
        Load any image from given path and resize it to be suitable for the UI.

        Args:
            file: Path to the image file.
            opener: Function to open the image with. `PIL.Image.open` by default.
        Returns:
            Image entity.
        """

        image = opener(file)
        return Image(image)

    @staticmethod
    def load_from_bytes(file_bytes, opener=PIL.Image.open):
        """
        Load any type of image from the given bytes object.

        Args:
            file_bytes: Image file as a bytes object.
            opener: Function to open the image with. `PIL.Image.open` by default.
        Returns:
            Image entity.
        """

        image = opener(io.BytesIO(file_bytes))
        return Image(image)

    def _resize_if_necessary(self):
        width, height = self.loaded_image.size
        scale = IMAGE_SIZE / max(width, height)
        if scale != 1.0:
            new_size = (int(width * scale), int(height * scale))
            self.loaded_image = self.loaded_image.resize(new_size)

    def as_png_bytes(self):
        """
        Encode this image as a PNG.

        Returns:
            A bytes object containing the PNG encoding of the associated image.
        """

        stream = io.BytesIO()
        self.loaded_image.save(stream, format="PNG")
        return stream.getvalue()
