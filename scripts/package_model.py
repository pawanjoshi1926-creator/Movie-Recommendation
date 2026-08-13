from pathlib import Path
import shutil


SOURCE_DIR = Path("artifacts")
MODEL_DIR = Path("model_package")

MODEL_DIR.mkdir(exist_ok=True)

files = [
    "movies.pkl",
    "similarity.pkl",
    "vectorizer.pkl"
]

for filename in files:

    source = SOURCE_DIR / filename
    destination = MODEL_DIR / filename

    if source.exists():
        shutil.copy2(source, destination)
        print(f"Copied: {filename}")
    else:
        print(f"Missing: {filename}")