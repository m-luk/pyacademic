import os
from pathlib import Path

INIT_PATH = Path(os.path.realpath(__file__))
SCRIPT_DIR = INIT_PATH.parent
DATA_DIR = SCRIPT_DIR / "data"