import PIL.Image

IMAGE_SIZE = 200

class Image:
    def __init__(self, image):
        self.image = image
        self.resize_if_necessary()

    @staticmethod
    def load_from_file(file):
        image = PIL.Image.open(file)
        return Image(image)

    def resize_if_necessary(self):
        width, height = self.image.size
        scale = IMAGE_SIZE / max(width, height)
        if scale != 1.0:
            new_size = (int(width * scale), int(height * scale))
            self.image = self.image.resize(new_size)


