from pathlib import Path
import sqlite3

path = Path("data", "tietokanta.db")
database_connection = sqlite3.connect(path)
database_connection.row_factory = sqlite3.Row
