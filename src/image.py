import PIL.Image

IMAGE_SIZE = 200

class Image:
    def __init__(self, image):
        self.loaded_image = image
        self._resize_if_necessary()

    @staticmethod
    def load_from_file(file, opener=PIL.Image.open):
        image = opener(file)
        return Image(image)

    def _resize_if_necessary(self):
        width, height = self.loaded_image.size
        scale = IMAGE_SIZE / max(width, height)
        if scale != 1.0:
            new_size = (int(width * scale), int(height * scale))
            self.loaded_image = self.loaded_image.resize(new_size)
