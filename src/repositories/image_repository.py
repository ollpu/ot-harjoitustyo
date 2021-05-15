from database import database_connection
from entities.image import Image

class ImageRepository:
    def __init__(self, db=database_connection, image_factory=Image):
        """
        Construct an ImageRepository.

        Args:
            db: Database connection to use.
            image_factory: Image class used for loading images from bytes.
        """

        self._db = db
        self._image_cache = {}
        self._image_factory = image_factory
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

        Args:
            image: An Image entity.
        Returns:
            The id of the stored image.
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
        Get an image object with the given ID, possibly deferring actually loading
        the image into memory.

        Args:
            image_id: ID to fetch with.
        Returns:
            The Image associated with this ID.
        """

        if image_id in self._image_cache:
            return self._image_cache[image_id]
        else:
            # Load immediately for now.
            cursor = self._db.cursor()
            cursor.execute("SELECT full_size FROM image WHERE id = ?;", (image_id,))
            row = cursor.fetchone()
            image = self._image_factory.load_from_bytes(row["full_size"])
            image.id = image_id
            return image

    def clear(self):
        """
        Clear the image repository. Leaves games referencing images in an invalid state.
        """

        cursor = self._db.cursor()
        cursor.execute("DELETE FROM image;")
        self._db.commit()
        self._image_cache.clear()

    def clear_cache(self):
        """
        Evict all images from the instance specific cache.
        """

        self._image_cache.clear()

default_image_repository = ImageRepository()
