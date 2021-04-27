from database import database_connection
from entities.image import Image

class ImageRepository:
    def __init__(self, db=database_connection):
        self._db = db
        self._image_cache = {}
        cursor = self._db.cursor()
        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS image (
                id INTEGER PRIMARY KEY,
                full_size BLOB,
                thumbnail BLOB
            );
            """
        )
        self._db.commit()

    def ensure_stored(self, image):
        """
        Stores the given image in the repository if it is not already stored.
        It is assumed that the contents of the image are never changed during
        its lifetime.

        Returns: The id of the stored image.
        """

        if not image.id:
            cursor = self._db.cursor()
            full_size_bin = image.as_png_bytes()
            cursor.execute("INSERT INTO image (full_size) VALUES (?);", (full_size_bin,))
            image.id = cursor.lastrowid
            self._db.commit()
        self._image_cache[image.id] = image
        return image.id

    def get_lazy(self, image_id):
        """
        Get an image object with the given id, possibly deferring actually loading
        the images.

        Returns: The Image associated with this id.
        """

        if image_id in self._image_cache:
            return self._image_cache[image_id]
        else:
            # Load immediately for now.
            cursor = self._db.cursor()
            cursor.execute("SELECT full_size FROM image WHERE id = ?;", (image_id,))
            row = cursor.fetchone()
            image = Image.load_from_bytes(row["full_size"])
            image.id = image_id
            return image

default_image_repository = ImageRepository()
