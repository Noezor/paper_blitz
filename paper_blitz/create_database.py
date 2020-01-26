from pathlib import Path

import paper_blitz.stack.model
from paper_blitz.config import db
import paper_blitz.articles.article


path_db = Path.cwd()/"paper_blitz"/Path("paper-blitz.db")

print(path_db)

if path_db.exists():
    print("DELETING OLD DATABASE")
    path_db.unlink()

db.create_all()