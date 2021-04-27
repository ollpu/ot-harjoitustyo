import tempfile
import sqlite3

db_file = tempfile.NamedTemporaryFile().name
database_connection = sqlite3.connect(db_file)
database_connection.row_factory = sqlite3.Row
database_connection.cursor().execute("PRAGMA foreign_keys = ON;")
