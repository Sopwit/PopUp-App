"""UI helper components, layout positioning, and widget factories."""

import tkinter as tk
from typing import Callable
from popupapp.config.theme import THEME


def center_window(
    win: tk.Tk | tk.Toplevel,
    width: int,
    height: int,
    parent: tk.Tk | tk.Toplevel | None = None,
) -> None:
    """Center a window relative to its parent or the primary display."""
    win.update_idletasks()
    if parent and parent.winfo_ismapped():
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_w = parent.winfo_width()
        parent_h = parent.winfo_height()
        pos_x = parent_x + (parent_w - width) // 2
        pos_y = parent_y + (parent_h - height) // 2
    else:
        screen_w = win.winfo_screenwidth()
        screen_h = win.winfo_screenheight()
        pos_x = (screen_w - width) // 2
        pos_y = (screen_h - height) // 2

    pos_x = max(0, pos_x)
    pos_y = max(0, pos_y)
    win.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    win.update_idletasks()


def create_styled_button(
    parent: tk.Widget,
    text: str,
    command: Callable[[], None],
    bg_color: str,
    hover_color: str,
    font: tuple[str, int, str] = THEME.FONT_BUTTON,
    width: int = 14,
    height: int = 1,
    fg_color: str = THEME.TEXT_WHITE,
) -> tk.Button:
    """Create a standardized modern flat button with responsive hover feedback."""
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg_color,
        activebackground=hover_color,
        fg=fg_color,
        activeforeground=fg_color,
        font=font,
        width=width,
        height=height,
        relief="flat",
        cursor="hand2",
        bd=0,
        highlightthickness=0,
    )
    btn.bind("<Enter>", lambda _e: btn.config(bg=hover_color))
    btn.bind("<Leave>", lambda _e: btn.config(bg=bg_color))
    return btn


def create_badge(
    parent: tk.Widget,
    text: str,
    bg_color: str = THEME.BADGE_BG,
    fg_color: str = THEME.BADGE_FG,
    font: tuple[str, int, str] = THEME.FONT_BADGE,
) -> tk.Label:
    """Create a status pill badge."""
    return tk.Label(
        parent,
        text=text,
        bg=bg_color,
        fg=fg_color,
        font=font,
        padx=8,
        pady=3,
        relief="flat",
    )
