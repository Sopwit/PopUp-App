"""Unit tests for internationalization catalog and language switching."""

from popupapp.i18n.translations import I18nManager, Locale, MESSAGES


def test_i18n_locales_completeness() -> None:
    tr_keys = set(MESSAGES[Locale.TR].keys())
    en_keys = set(MESSAGES[Locale.EN].keys())
    assert tr_keys == en_keys
    assert len(tr_keys) >= 15


def test_i18n_manager_translations() -> None:
    manager = I18nManager(default_locale=Locale.TR)
    assert manager.t("btn_exit") == "Çıkış"
    assert manager.t("btn_greet") == "Selamla"
    assert manager.t("greeting_personalized", name="Emir") == "Merhaba, Emir!"

    manager.set_locale(Locale.EN)
    assert manager.t("btn_exit") == "Exit"
    assert manager.t("btn_greet") == "Greet"
    assert manager.t("greeting_personalized", name="Emir") == "Hello, Emir!"


def test_i18n_toggle_and_listeners() -> None:
    manager = I18nManager(default_locale=Locale.TR)
    received_locales = []

    def on_change(loc: Locale) -> None:
        received_locales.append(loc)

    manager.add_listener(on_change)
    manager.toggle_locale()
    assert manager.current_locale == Locale.EN
    assert received_locales == [Locale.EN]

    manager.toggle_locale()
    assert manager.current_locale == Locale.TR
    assert received_locales == [Locale.EN, Locale.TR]

    manager.remove_listener(on_change)
    manager.toggle_locale()
    assert len(received_locales) == 2
