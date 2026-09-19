import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_config():
    with open(ROOT / "config.json", encoding="utf-8") as file:
        return json.load(file)


def ensure_directories():
    for path in [
        ROOT / "data" / "raw",
        ROOT / "data" / "processed",
        ROOT / "outputs" / "reports",
        ROOT / "outputs" / "charts",
    ]:
        path.mkdir(parents=True, exist_ok=True)
