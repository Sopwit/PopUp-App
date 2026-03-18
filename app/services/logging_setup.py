import logging
import os
import sys
from pathlib import Path

APP_NAME = "super_popup_app"
LOG_FILE_NAME = "app_log.txt"


def resolve_log_dir(
    platform_name: str | None = None,
    home_dir: str | None = None,
    appdata_dir: str | None = None,
) -> Path:
    platform_name = platform_name or sys.platform
    home = Path(home_dir) if home_dir else Path.home()

    if platform_name.startswith("win"):
        appdata = appdata_dir or os.getenv("APPDATA")
        base_dir = Path(appdata) if appdata else home / "AppData" / "Roaming"
        return base_dir / APP_NAME

    if platform_name == "darwin":
        return home / "Library" / "Application Support" / APP_NAME

    return home / ".local" / "share" / APP_NAME


def configure_logging() -> logging.Logger:
    log_dir = resolve_log_dir()
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / LOG_FILE_NAME

    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(APP_NAME)
    logger.info("--- Uygulama Baslatildi ---")
    return logger
