from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    force=True  
)

FILES = [
    ".github/workflows/.gitkeep",
    "backend/ingest_data.py",
    "backend/model.py",
    "static/app.js",
    "static/style.css",
    "app.py",
    ".env",
    "Dockerfile",
    "requirements.txt",
    "templates/index.html",
]

print("✅ template.py started")
created = 0

for f in FILES:
    path = Path(f)

    # create directories
    path.parent.mkdir(parents=True, exist_ok=True)

    # create file if missing or empty
    if (not path.exists()) or (path.stat().st_size == 0):
        path.touch()
        logging.info(f"Created/Ensured: {path}")
        created += 1
    else:
        logging.info(f"Already exists: {path}")

print(f" Files touched/created: {created}")
