"""Legacy import bridge for app.main."""

import sys
from pathlib import Path

_SRC_DIR = str(Path(__file__).resolve().parent.parent / "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from popupapp.ui.app import run

if __name__ == "__main__":
    run()
