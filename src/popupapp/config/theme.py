"""UI Theme definition and color palette inspired by modern dark interfaces."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UITheme:
    """Nordic dark cyber aesthetic with vibrant accents and micro-elevation."""

    # Backgrounds
    BG_CANVAS: str = "#131622"
    BG_CARD: str = "#1c2030"
    BG_CARD_ELEVATED: str = "#252b42"
    BG_POPUP: str = "#181c2c"

    # Borders & Dividers
    BORDER_SUBTLE: str = "#2e3654"
    BORDER_ACCENT: str = "#06b6d4"

    # Brand & Action Colors
    ACCENT_PRIMARY: str = "#06b6d4"          # Cyan
    ACCENT_PRIMARY_HOVER: str = "#0891b2"
    ACCENT_SECONDARY: str = "#f59e0b"        # Amber
    ACCENT_SECONDARY_HOVER: str = "#d97706"
    ACCENT_DANGER: str = "#ef4444"           # Red
    ACCENT_DANGER_HOVER: str = "#dc2626"
    ACCENT_SUCCESS: str = "#10b981"          # Emerald
    ACCENT_SUCCESS_HOVER: str = "#059669"

    # Text Colors
    TEXT_WHITE: str = "#f8fafc"
    TEXT_PRIMARY: str = "#e2e8f0"
    TEXT_SECONDARY: str = "#94a3b8"
    TEXT_MUTED: str = "#64748b"

    # Badges & Buttons
    BADGE_BG: str = "#064e3b"
    BADGE_FG: str = "#34d399"
    LANG_BTN_BG: str = "#252b42"
    LANG_BTN_HOVER: str = "#333b5c"
    LANG_BTN_ACTIVE_BG: str = "#06b6d4"
    LANG_BTN_ACTIVE_FG: str = "#ffffff"

    # Typography
    FONT_HERO: tuple[str, int, str] = ("Helvetica", 18, "bold")
    FONT_SUBTITLE: tuple[str, int, str] = ("Helvetica", 10, "normal")
    FONT_BADGE: tuple[str, int, str] = ("Helvetica", 9, "bold")
    FONT_BUTTON: tuple[str, int, str] = ("Helvetica", 11, "bold")
    FONT_BUTTON_SM: tuple[str, int, str] = ("Helvetica", 9, "bold")
    FONT_FOOTER: tuple[str, int, str] = ("Helvetica", 9, "normal")
    FONT_POPUP_TITLE: tuple[str, int, str] = ("Helvetica", 14, "bold")
    FONT_POPUP_TEXT: tuple[str, int, str] = ("Helvetica", 12, "bold")


THEME = UITheme()
