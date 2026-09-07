"""UI helper components, custom modal dialogs, layout positioning, and widget factories."""

import tkinter as tk
from typing import Callable
from popupapp.config.theme import THEME
from popupapp.i18n.translations import I18N


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


def ask_custom_string(
    parent: tk.Tk | tk.Toplevel,
    title: str,
    prompt: str,
    icon_image: tk.PhotoImage | None = None,
) -> str | None:
    """Show a custom themed modal dialog asking for user string input."""
    dialog = tk.Toplevel(parent)
    dialog.title(title)
    dialog.configure(bg=THEME.BG_POPUP)
    dialog.resizable(False, False)
    dialog.transient(parent)

    if icon_image:
        try:
            dialog.iconphoto(False, icon_image)
        except Exception:
            pass

    result: list[str | None] = [None]

    card = tk.Frame(
        dialog,
        bg=THEME.BG_CARD,
        highlightbackground=THEME.BORDER_SUBTLE,
        highlightthickness=1,
        padx=20,
        pady=16,
    )
    card.pack(fill="both", expand=True, padx=14, pady=14)

    lbl_prompt = tk.Label(
        card,
        text=prompt,
        font=THEME.FONT_POPUP_TEXT,
        fg=THEME.TEXT_WHITE,
        bg=THEME.BG_CARD,
    )
    lbl_prompt.pack(anchor="w", pady=(2, 10))

    entry_var = tk.StringVar()
    entry = tk.Entry(
        card,
        textvariable=entry_var,
        font=THEME.FONT_POPUP_TEXT,
        bg=THEME.BG_CANVAS,
        fg=THEME.TEXT_WHITE,
        insertbackground=THEME.ACCENT_PRIMARY,
        relief="flat",
        highlightthickness=1,
        highlightbackground=THEME.BORDER_SUBTLE,
        highlightcolor=THEME.ACCENT_PRIMARY,
    )
    entry.pack(fill="x", pady=(0, 16), ipady=4)

    def on_submit() -> None:
        result[0] = entry_var.get()
        dialog.destroy()

    def on_cancel() -> None:
        result[0] = None
        dialog.destroy()

    btn_row = tk.Frame(card, bg=THEME.BG_CARD)
    btn_row.pack(fill="x")

    btn_submit = create_styled_button(
        parent=btn_row,
        text=I18N.t("btn_ok"),
        command=on_submit,
        bg_color=THEME.ACCENT_PRIMARY,
        hover_color=THEME.ACCENT_PRIMARY_HOVER,
        font=THEME.FONT_BUTTON,
        width=10,
    )
    btn_submit.pack(side="right", padx=(8, 0))

    btn_cancel = create_styled_button(
        parent=btn_row,
        text=I18N.t("btn_cancel"),
        command=on_cancel,
        bg_color=THEME.ACCENT_DANGER,
        hover_color=THEME.ACCENT_DANGER_HOVER,
        font=THEME.FONT_BUTTON,
        width=10,
    )
    btn_cancel.pack(side="right")

    dialog.protocol("WM_DELETE_WINDOW", on_cancel)
    dialog.bind("<Return>", lambda _e: on_submit())
    dialog.bind("<Escape>", lambda _e: on_cancel())

    center_window(dialog, 380, 200, parent=parent)
    entry.focus_set()
    dialog.wait_window()

    return result[0]
