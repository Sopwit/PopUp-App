"""Integration tests for UI components, custom dialogs, and geometry positioning."""

import tkinter as tk
from popupapp.config.theme import THEME
from popupapp.ui.components import (
    ask_custom_string,
    center_window,
    create_badge,
    create_styled_button,
)


def test_center_window_geometry(tk_root) -> None:
    win = tk.Toplevel(tk_root)
    center_window(win, 300, 200, parent=tk_root)
    win.update()
    geom = win.geometry()
    assert "300x200" in geom
    win.destroy()


def test_create_styled_button_hover_events(tk_root) -> None:
    clicked = []
    btn = create_styled_button(
        parent=tk_root,
        text="Click Me",
        command=lambda: clicked.append(True),
        bg_color=THEME.ACCENT_PRIMARY,
        hover_color=THEME.ACCENT_PRIMARY_HOVER,
    )
    btn.pack()
    btn.invoke()
    assert clicked == [True]
    btn.destroy()


def test_create_badge(tk_root) -> None:
    badge = create_badge(parent=tk_root, text="● Ready")
    assert badge.cget("text") == "● Ready"
    assert badge.cget("bg") == THEME.BADGE_BG
