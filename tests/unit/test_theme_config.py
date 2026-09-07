"""Unit tests for configuration limits and theme aesthetics."""

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
from popupapp.config.theme import THEME


def test_config_constants_validity() -> None:
    assert APP_NAME == "super_popup_app"
    assert "Popup" in APP_DISPLAY_NAME
    assert LOG_FILE_NAME == "app_log.txt"
    assert MAX_NAME_LENGTH == 50
    assert MAX_LOG_BYTES >= 1024
    assert BACKUP_COUNT >= 1
    assert DEFAULT_DIR_PERMISSIONS == 0o700
    assert MAIN_WINDOW_WIDTH > POPUP_WINDOW_WIDTH
    assert MAIN_WINDOW_HEIGHT > POPUP_WINDOW_HEIGHT


def test_theme_color_palette_hex_format() -> None:
    assert THEME.BG_CANVAS.startswith("#")
    assert THEME.BG_CARD.startswith("#")
    assert THEME.BG_POPUP.startswith("#")
    assert THEME.ACCENT_PRIMARY.startswith("#")
    assert THEME.ACCENT_DANGER.startswith("#")
    assert THEME.ACCENT_SECONDARY.startswith("#")


def test_theme_typography() -> None:
    for font_spec in (
        THEME.FONT_HERO,
        THEME.FONT_BUTTON,
        THEME.FONT_POPUP_TITLE,
        THEME.FONT_POPUP_TEXT,
    ):
        assert len(font_spec) >= 2
        assert isinstance(font_spec[0], str)
        assert isinstance(font_spec[1], int)
