import os
from pathlib import Path
import sqlite3

path = Path("data", "tietokanta.db")
configured_path = os.getenv("LUHA_TIETOKANTA") or path
database_connection = sqlite3.connect(configured_path)
database_connection.row_factory = sqlite3.Row
database_connection.cursor().execute("PRAGMA foreign_keys = ON;")
