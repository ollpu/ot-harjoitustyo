from database import database_connection
from repositories.image_repository import default_image_repository
from entities.game import Game
from entities.round import Round

class GameRepository:
    def __init__(self, db=database_connection, image_repo=default_image_repository):
        self._db = db
        self._image_repository = image_repo
        cursor = self._db.cursor()
        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS game (
                id INTEGER PRIMARY KEY,
                name TEXT
            );
            CREATE TABLE IF NOT EXISTS round (
                id INTEGER PRIMARY KEY,
                game_id INTEGER,
                position INTEGER,
                FOREIGN KEY(game_id) REFERENCES game(id) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS image_pair (
                round_id INTEGER,
                caption TEXT,
                image_id INTEGER,
                FOREIGN KEY(round_id) REFERENCES round(id) ON DELETE CASCADE
            );
            """
        )
        self._db.commit()

    def store(self, game):
        """
        Store a new or updated a game.
        """

        cursor = self._db.cursor()
        if game.id is not None:
            cursor.execute("DELETE FROM game WHERE id = ?;", (game.id,))
        cursor.execute("INSERT INTO game (name) VALUES (?)", (game.name,))
        game.id = cursor.lastrowid
        for position, g_round in enumerate(game.rounds):
            cursor.execute("INSERT INTO round (game_id, position) VALUES (?, ?)",
                           (game.id, position))
            g_round.id = cursor.lastrowid
            for caption, image in g_round.pairs:
                image_id = self._image_repository.ensure_stored(image)
                cursor.execute(
                    "INSERT INTO image_pair (round_id, caption, image_id) VALUES (?, ?, ?)",
                    (g_round.id, caption, image_id)
                )
        # There may now be dangling (unused) images. They should be dealt with elsewhere.
        self._db.commit()

    def remove(self, game):
        if game.id is None:
            # Not stored in database, ignore
            pass
        else:
            cursor = self._db.cursor()
            cursor.execute("DELETE FROM game WHERE id = ?;", (game.id,))
            self._db.commit()

    def all(self):
        """
        Get all games stored in the repository.
        """

        games = {}
        cursor = self._db.cursor()
        cursor.execute("SELECT id, name FROM game ORDER BY id;")
        for row in cursor.fetchall():
            game = Game(row["name"], [])
            game.id = row["id"]
            games[game.id] = game

        rounds = {}
        cursor.execute("SELECT id, game_id FROM round ORDER BY game_id, position;")
        for row in cursor.fetchall():
            g_round = Round([])
            g_round.id = row["id"]
            games[row["game_id"]].rounds.append(g_round)
            rounds[g_round.id] = g_round

        images = []
        cursor.execute("SELECT round_id, caption, image_id FROM image_pair;")
        for row in cursor.fetchall():
            image = self._image_repository.get_lazy(row["image_id"])
            images.append(image)
            pair = (row["caption"], image)
            rounds[row["round_id"]].pairs.append(pair)

        # self._image_repository.load_thumbnails(images)

        return list(games.values())

    def clear(self):
        """
        Clear the repository, removing all games. Images will be left dangling.
        """

        cursor = self._db.cursor()
        cursor.execute("DELETE FROM game;")
        self._db.commit()

default_game_repository = GameRepository()
