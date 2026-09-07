"""Integration tests for PopupApp lifecycle, dialogs, modal state, and i18n switching."""

import tkinter as tk
from unittest.mock import MagicMock

from popupapp.i18n.translations import I18N, Locale
from popupapp.ui.app import PopupApp


def test_app_lifecycle_open_close(tk_root) -> None:
    logger = MagicMock()
    app = PopupApp(logger=logger, root=tk_root)

    app._open_popup(message="Hello Unit Test", close_log="Unit test popup closed")
    assert app._active_popup is not None
    assert app._active_popup.winfo_exists()

    # Reopening should close the prior popup safely
    old_popup = app._active_popup
    app._open_popup(message="Second Popup", close_log="Second popup closed")
    assert app._active_popup is not old_popup
    assert not old_popup.winfo_exists()

    app.on_close()
    assert logger.info.called


def test_app_language_switching(tk_root) -> None:
    logger = MagicMock()
    app = PopupApp(logger=logger, root=tk_root)

    app.switch_language(Locale.EN)
    assert I18N.current_locale == Locale.EN
    assert app.root.title() == "Super Modern Popup App"

    app.switch_language(Locale.TR)
    assert I18N.current_locale == Locale.TR
    assert app.root.title() == "Super Modern Popup Uygulaması"


def test_app_modern_popup_flow(monkeypatch, tk_root) -> None:
    logger = MagicMock()
    app = PopupApp(logger=logger, root=tk_root)

    # 1. Dialog cancelled
    monkeypatch.setattr("tkinter.simpledialog.askstring", lambda *a, **kw: None)
    app.modern_popup()
    assert app._active_popup is None

    # 2. Empty input
    monkeypatch.setattr("tkinter.simpledialog.askstring", lambda *a, **kw: "   ")
    app.modern_popup()
    assert app._active_popup is not None
    assert app._active_popup.winfo_exists()

    # 3. Valid name
    monkeypatch.setattr("tkinter.simpledialog.askstring", lambda *a, **kw: "Emir")
    app.modern_popup()
    assert app._active_popup is not None
    assert app._active_popup.winfo_exists()


def test_app_exception_handling_in_dialog(monkeypatch, tk_root) -> None:
    logger = MagicMock()
    app = PopupApp(logger=logger, root=tk_root)

    def raise_err(*args, **kwargs):
        raise RuntimeError("Simulated Dialog Failure")

    monkeypatch.setattr("tkinter.simpledialog.askstring", raise_err)
    app.modern_popup()
    assert logger.error.called
