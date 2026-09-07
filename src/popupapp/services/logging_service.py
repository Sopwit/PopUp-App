"""Cross-platform logging service with rotating file handlers and hardened permissions."""

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from popupapp.config.constants import (
    APP_NAME,
    BACKUP_COUNT,
    DEFAULT_DIR_PERMISSIONS,
    LOG_FILE_NAME,
    MAX_LOG_BYTES,
)


def resolve_log_dir(
    platform_name: str | None = None,
    home_dir: str | None = None,
    appdata_dir: str | None = None,
) -> Path:
    """Determine the standard OS-specific directory for application logs.

    - Windows: %APPDATA%\\super_popup_app (or ~/AppData/Roaming/super_popup_app)
    - macOS: ~/Library/Application Support/super_popup_app
    - Linux/BSD/Other: ~/.local/share/super_popup_app (XDG data home)
    """
    platform_name = platform_name or sys.platform
    home = Path(home_dir) if home_dir else Path.home()

    if platform_name.startswith("win"):
        appdata = os.getenv("APPDATA") if appdata_dir is None else appdata_dir
        base_dir = Path(appdata) if appdata else home / "AppData" / "Roaming"
        return base_dir / APP_NAME

    if platform_name == "darwin":
        return home / "Library" / "Application Support" / APP_NAME

    return home / ".local" / "share" / APP_NAME


def configure_logging(
    max_bytes: int = MAX_LOG_BYTES,
    backup_count: int = BACKUP_COUNT,
    log_level: int = logging.INFO,
) -> logging.Logger:
    """Initialize or reuse the application logger with rotating file storage."""
    log_dir = resolve_log_dir()
    os.makedirs(log_dir, mode=DEFAULT_DIR_PERMISSIONS, exist_ok=True)
    log_file = log_dir / LOG_FILE_NAME

    logger = logging.getLogger(APP_NAME)
    logger.setLevel(log_level)
    logger.propagate = False

    has_target_handler = False
    for handler in list(logger.handlers):
        if not isinstance(handler, logging.FileHandler):
            continue

        if Path(handler.baseFilename).resolve() == log_file.resolve():
            has_target_handler = True
            continue

        logger.removeHandler(handler)
        handler.close()

    if not has_target_handler:
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(file_handler)

    logger.info("--- Uygulama Baslatildi ---")
    return logger
