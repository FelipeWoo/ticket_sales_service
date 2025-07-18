import sqlite3
from pathlib import Path

def get_connection(path: Path):
    return sqlite3.connect(path)