import sqlite3
from pathlib import Path


# Project root: study-planner/
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Database directory: study-planner/data/
DATABASE_DIR = PROJECT_ROOT / "data"
DATABASE_DIR.mkdir(exist_ok=True)

# Database file: study-planner/data/study_planner.db
DATABASE_PATH = DATABASE_DIR / "study_planner.db"


def get_connection() -> sqlite3.Connection:
    """Create and return a connection to the application database."""
    connection = sqlite3.connect(DATABASE_PATH)

    # Allows rows to be accessed by column name as well as index.
    connection.row_factory = sqlite3.Row

    # Enforce foreign-key relationships in SQLite.
    connection.execute("PRAGMA foreign_keys = ON")

    return connection