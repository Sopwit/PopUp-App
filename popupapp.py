#!/usr/bin/env python3
"""Root executable entry point for Super Modern Popup Application."""

import sys
from pathlib import Path

# Ensure src/ is on sys.path before local package resolution
_SRC_DIR = str(Path(__file__).resolve().parent / "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from popupapp.ui.app import run

if __name__ == "__main__":
    run()
