
from pathlib import Path

ENTRY_WORD = "ariandhykevz"

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ENTRY_WORD, encoding="utf-8")
