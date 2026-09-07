"""Configuration and theming exports."""

from popupapp.config.constants import (
    APP_DISPLAY_NAME,
    APP_NAME,
    BACKUP_COUNT,
    DEFAULT_DIR_PERMISSIONS,
    LOG_FILE_NAME,
    MAIN_WINDOW_HEIGHT,
    MAIN_WINDOW_WIDTH,
    MAX_LOG_BYTES,
    MAX_NAME_LENGTH,
    POPUP_WINDOW_HEIGHT,
    POPUP_WINDOW_WIDTH,
)
from popupapp.config.theme import THEME, UITheme

__all__ = [
    "APP_NAME",
    "APP_DISPLAY_NAME",
    "LOG_FILE_NAME",
    "MAX_NAME_LENGTH",
    "MAX_LOG_BYTES",
    "BACKUP_COUNT",
    "DEFAULT_DIR_PERMISSIONS",
    "MAIN_WINDOW_WIDTH",
    "MAIN_WINDOW_HEIGHT",
    "POPUP_WINDOW_WIDTH",
    "POPUP_WINDOW_HEIGHT",
    "THEME",
    "UITheme",
]
