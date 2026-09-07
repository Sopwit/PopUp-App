"""Main desktop GUI Application controller with custom themed dialogs, reactive i18n, and modal popups."""

import logging
from pathlib import Path
import tkinter as tk

from popupapp.config.constants import (
    MAIN_WINDOW_HEIGHT,
    MAIN_WINDOW_WIDTH,
    MAX_NAME_LENGTH,
    POPUP_WINDOW_HEIGHT,
    POPUP_WINDOW_WIDTH,
)
from popupapp.config.theme import THEME
from popupapp.core.sanitization import sanitize_input
from popupapp.i18n.translations import I18N, Locale
from popupapp.services.logging_service import configure_logging
from popupapp.ui.components import ask_custom_string, center_window, create_styled_button


class PopupApp:
    """Primary Tkinter application managing main window lifecycle, reactive i18n, and custom modals."""

    def __init__(self, logger: logging.Logger, root: tk.Tk | None = None) -> None:
        self.logger = logger
        self.root = root if root is not None else tk.Tk()
        self.root.configure(bg=THEME.BG_CANVAS)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self._active_popup: tk.Toplevel | None = None
        self._icon_image: tk.PhotoImage | None = None

        # Reactive status state
        self._status_key: str = "status_ready"
        self._status_kwargs: dict[str, object] = {}

        # Widget references for reactive i18n updating
        self._lbl_title: tk.Label | None = None
        self._lbl_subtitle: tk.Label | None = None
        self._lbl_status: tk.Label | None = None
        self._btn_greet: tk.Button | None = None
        self._btn_exit: tk.Button | None = None
        self._btn_lang_toggle: tk.Button | None = None

        self._set_app_icon()
        self._build_ui()
        self._apply_language(I18N.current_locale)
        I18N.add_listener(self._apply_language)

        center_window(self.root, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
        self._bind_shortcuts()

    def _set_app_icon(self) -> None:
        """Discover and bind application icon if present."""
        try:
            possible_paths = [
                Path(__file__).resolve().parent.parent.parent.parent / "logo.png",
                Path(__file__).resolve().parent.parent / "logo.png",
                Path.cwd() / "logo.png",
            ]
            for icon_path in possible_paths:
                if icon_path.exists():
                    self._icon_image = tk.PhotoImage(file=str(icon_path))
                    self.root.iconphoto(False, self._icon_image)
                    break
        except Exception as exc:
            self.logger.debug("Ikon yuklenemedi: %s", exc)

    def _bind_shortcuts(self) -> None:
        self.root.bind("<Escape>", lambda _e: self.on_close())
        self.root.bind("<Return>", lambda _e: self.modern_popup())

    def _build_ui(self) -> None:
        # Main Container
        main_container = tk.Frame(self.root, bg=THEME.BG_CANVAS)
        main_container.pack(fill="both", expand=True, padx=24, pady=16)

        # 1. Top Bar: Language Switcher Button
        top_bar = tk.Frame(main_container, bg=THEME.BG_CANVAS)
        top_bar.pack(fill="x", pady=(0, 4))

        self._btn_lang_toggle = create_styled_button(
            parent=top_bar,
            text=I18N.t("lang_toggle_btn"),
            command=self.toggle_language,
            bg_color=THEME.LANG_BTN_BG,
            hover_color=THEME.LANG_BTN_HOVER,
            font=THEME.FONT_BUTTON_SM,
            width=12,
        )
        self._btn_lang_toggle.pack(side="right")

        # 2. Hero Header Section
        self._lbl_title = tk.Label(
            main_container,
            text=I18N.t("app_title"),
            font=THEME.FONT_HERO,
            fg=THEME.TEXT_WHITE,
            bg=THEME.BG_CANVAS,
        )
        self._lbl_title.pack(anchor="center", pady=(4, 2))

        self._lbl_subtitle = tk.Label(
            main_container,
            text=I18N.t("app_subtitle"),
            font=THEME.FONT_SUBTITLE,
            fg=THEME.TEXT_SECONDARY,
            bg=THEME.BG_CANVAS,
        )
        self._lbl_subtitle.pack(anchor="center", pady=(0, 14))

        # 3. Main Action Card Frame
        card = tk.Frame(
            main_container,
            bg=THEME.BG_CARD,
            highlightbackground=THEME.BORDER_SUBTLE,
            highlightthickness=1,
            padx=16,
            pady=16,
        )
        card.pack(fill="x", pady=4)

        btn_row = tk.Frame(card, bg=THEME.BG_CARD)
        btn_row.pack(pady=4)

        self._btn_greet = create_styled_button(
            parent=btn_row,
            text=I18N.t("btn_greet"),
            command=self.modern_popup,
            bg_color=THEME.ACCENT_PRIMARY,
            hover_color=THEME.ACCENT_PRIMARY_HOVER,
            font=THEME.FONT_BUTTON,
            width=15,
            height=1,
        )
        self._btn_greet.pack(side="left", padx=12)

        self._btn_exit = create_styled_button(
            parent=btn_row,
            text=I18N.t("btn_exit"),
            command=self.on_close,
            bg_color=THEME.ACCENT_DANGER,
            hover_color=THEME.ACCENT_DANGER_HOVER,
            font=THEME.FONT_BUTTON,
            width=15,
            height=1,
        )
        self._btn_exit.pack(side="left", padx=12)

        self._lbl_status = tk.Label(
            card,
            text=I18N.t("status_ready"),
            font=THEME.FONT_SUBTITLE,
            fg=THEME.TEXT_MUTED,
            bg=THEME.BG_CARD,
        )
        self._lbl_status.pack(pady=(12, 2))

    def toggle_language(self) -> None:
        """Toggle between Turkish and English with instant UI update."""
        new_locale = I18N.toggle_locale()
        self.logger.info("Dil secimi degistirildi: %s", new_locale.value.upper())

    def switch_language(self, locale: Locale) -> None:
        """Switch language and update UI reactively."""
        I18N.set_locale(locale)
        self.logger.info("Dil secimi guncellendi: %s", locale.value.upper())

    def _apply_language(self, _locale: Locale) -> None:
        """Update all reactive texts based on active locale."""
        self.root.title(I18N.t("app_title"))
        if self._btn_lang_toggle:
            self._btn_lang_toggle.config(text=I18N.t("lang_toggle_btn"))
        if self._lbl_title:
            self._lbl_title.config(text=I18N.t("app_title"))
        if self._lbl_subtitle:
            self._lbl_subtitle.config(text=I18N.t("app_subtitle"))
        if self._btn_greet:
            self._btn_greet.config(text=I18N.t("btn_greet"))
        if self._btn_exit:
            self._btn_exit.config(text=I18N.t("btn_exit"))
        if self._lbl_status:
            self._lbl_status.config(
                text=I18N.t(self._status_key, **self._status_kwargs),
                fg=THEME.TEXT_SECONDARY if self._status_key != "status_ready" else THEME.TEXT_MUTED,
            )

    def set_status(self, key: str, **kwargs: object) -> None:
        """Update inline status banner and persist status key for reactive language updates."""
        self._status_key = key
        self._status_kwargs = kwargs
        if self._lbl_status:
            self._lbl_status.config(
                text=I18N.t(key, **kwargs),
                fg=THEME.TEXT_SECONDARY if key != "status_ready" else THEME.TEXT_MUTED,
            )

    def on_close(self) -> None:
        """Gracefully terminate active popups and root window."""
        self.logger.info(I18N.t("log_app_closed"))
        if self._active_popup and self._active_popup.winfo_exists():
            try:
                self._active_popup.destroy()
            except Exception:
                pass
            self._active_popup = None
        self.root.destroy()

    def _open_popup(self, message: str, close_log: str) -> None:
        """Spawn a modal greeting dialog centered on top of parent window."""
        if self._active_popup and self._active_popup.winfo_exists():
            try:
                self._active_popup.destroy()
            except Exception:
                pass
            self._active_popup = None

        popup = tk.Toplevel(self.root)
        self._active_popup = popup
        popup.title(I18N.t("popup_title"))
        popup.configure(bg=THEME.BG_POPUP)
        popup.resizable(False, False)
        popup.transient(self.root)

        if self._icon_image:
            try:
                popup.iconphoto(False, self._icon_image)
            except Exception:
                pass

        card = tk.Frame(
            popup,
            bg=THEME.BG_CARD,
            highlightbackground=THEME.BORDER_SUBTLE,
            highlightthickness=1,
            padx=20,
            pady=16,
        )
        card.pack(fill="both", expand=True, padx=16, pady=16)

        mesaj = tk.Label(
            card,
            text=message,
            font=THEME.FONT_POPUP_TEXT,
            fg=THEME.ACCENT_PRIMARY,
            bg=THEME.BG_CARD,
            wraplength=320,
            justify="center",
        )
        mesaj.pack(pady=(12, 16), padx=10)

        def popup_kapat() -> None:
            self.logger.info(close_log)
            if self._active_popup == popup:
                self._active_popup = None
            try:
                popup.destroy()
            except Exception:
                pass

        kapat_butonu = create_styled_button(
            parent=card,
            text=I18N.t("btn_close"),
            command=popup_kapat,
            bg_color=THEME.ACCENT_SECONDARY,
            hover_color=THEME.ACCENT_SECONDARY_HOVER,
            font=THEME.FONT_BUTTON,
            width=12,
        )
        kapat_butonu.pack(pady=4)
        kapat_butonu.bind("<Button-1>", lambda _e: popup_kapat())
        kapat_butonu.bind("<Return>", lambda _e: popup_kapat())
        kapat_butonu.bind("<space>", lambda _e: popup_kapat())

        popup.protocol("WM_DELETE_WINDOW", popup_kapat)
        popup.bind("<Return>", lambda _e: popup_kapat())
        popup.bind("<Escape>", lambda _e: popup_kapat())
        popup.bind("<space>", lambda _e: popup_kapat())

        center_window(popup, POPUP_WINDOW_WIDTH, POPUP_WINDOW_HEIGHT, parent=self.root)
        popup.lift()
        popup.focus_force()
        kapat_butonu.focus_set()

    def modern_popup(self) -> None:
        """Prompt user for name input via custom themed modal and present greeting."""
        self.logger.info(I18N.t("log_greet_clicked"))
        try:
            isim = ask_custom_string(
                parent=self.root,
                title=I18N.t("dialog_title"),
                prompt=I18N.t("dialog_prompt"),
                icon_image=self._icon_image,
            )
            if isim is None:
                self.logger.info(I18N.t("log_dialog_cancelled"))
                self.set_status("status_cancelled")
                return

            temiz_isim = sanitize_input(isim, max_length=MAX_NAME_LENGTH)
            if temiz_isim:
                self.logger.info(I18N.t("log_name_entered", name=temiz_isim))
                self.set_status("status_greeted", name=temiz_isim)
                self._open_popup(
                    message=I18N.t("greeting_personalized", name=temiz_isim),
                    close_log=I18N.t("log_popup_closed", name=temiz_isim),
                )
                return

            self.logger.warning(I18N.t("log_empty_name"))
            self.set_status("status_ready")
            self._open_popup(
                message=I18N.t("greeting_anonymous"),
                close_log=I18N.t("log_anon_popup_closed"),
            )
        except Exception as exc:
            self.logger.error("Popup olusturulurken hata: %s", exc, exc_info=True)
            self.set_status("status_error", error=str(exc))

    def run(self) -> None:
        """Start the GUI event loop with top-level error trapping."""
        try:
            self.root.mainloop()
        except Exception as exc:
            self.logger.critical("Uygulama beklenmedik bir hata ile coktu: %s", exc, exc_info=True)
            print(f"Kritik Hata: {exc}")


def run() -> None:
    """Application bootstrap helper."""
    logger = configure_logging()
    app = PopupApp(logger)
    app.run()
