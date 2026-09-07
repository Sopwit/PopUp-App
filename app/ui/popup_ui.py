"""Legacy import bridge for app.ui.popup_ui."""

import sys
from pathlib import Path

_SRC_DIR = str(Path(__file__).resolve().parent.parent.parent / "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from popupapp.config.theme import THEME, UITheme
from popupapp.core.sanitization import sanitize_input
from popupapp.ui.app import PopupApp
from popupapp.ui.components import center_window, create_styled_button

__all__ = [
    "PopupApp",
    "THEME",
    "UITheme",
    "sanitize_input",
    "center_window",
    "create_styled_button",
]
