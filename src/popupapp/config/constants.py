"""Central application constants and configuration limits."""

APP_NAME: str = "super_popup_app"
APP_DISPLAY_NAME: str = "Super Modern Popup Uygulamasi"
LOG_FILE_NAME: str = "app_log.txt"

# Security & Validation limits
MAX_NAME_LENGTH: int = 50
MAX_LOG_BYTES: int = 1_048_576  # 1 MB
BACKUP_COUNT: int = 3
DEFAULT_DIR_PERMISSIONS: int = 0o700

# Optimized window geometry
MAIN_WINDOW_WIDTH: int = 520
MAIN_WINDOW_HEIGHT: int = 265
POPUP_WINDOW_WIDTH: int = 360
POPUP_WINDOW_HEIGHT: int = 190
