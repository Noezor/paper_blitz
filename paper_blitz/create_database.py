from pathlib import Path

from config import db
from articles.article import Article

path_db = Path("paper-blitz.db")

if path_db.exists():
    path_db.unlink()

db.create_all()