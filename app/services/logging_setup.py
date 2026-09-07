"""Legacy import bridge for app.services.logging_setup."""

import sys
from pathlib import Path

_SRC_DIR = str(Path(__file__).resolve().parent.parent.parent / "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from popupapp.config.constants import (
    APP_NAME,
    BACKUP_COUNT,
    LOG_FILE_NAME,
    MAX_LOG_BYTES,
)
from popupapp.services.logging_service import configure_logging, resolve_log_dir

__all__ = [
    "APP_NAME",
    "LOG_FILE_NAME",
    "MAX_LOG_BYTES",
    "BACKUP_COUNT",
    "configure_logging",
    "resolve_log_dir",
]
