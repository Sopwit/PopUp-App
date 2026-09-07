"""Internationalization (i18n) and localization catalog."""

from enum import StrEnum
from typing import Callable


class Locale(StrEnum):
    TR = "tr"
    EN = "en"


MESSAGES: dict[Locale, dict[str, str]] = {
    Locale.TR: {
        "app_title": "Super Modern Popup Uygulaması",
        "app_subtitle": "Hafif, Güvenli ve Hızlı Karşılama Deneyimi",
        "btn_greet": "Selamla",
        "btn_exit": "Çıkış",
        "btn_close": "Kapat",
        "btn_ok": "Tamam",
        "btn_cancel": "İptal",
        "lang_toggle_btn": "🌐 TR ⇄ EN",
        "dialog_title": "İsim Girişi",
        "dialog_prompt": "Lütfen adınızı giriniz:",
        "popup_title": "Karşılama",
        "greeting_personalized": "Merhaba, {name}!",
        "greeting_anonymous": "Merhaba! Uygulamamıza Hoş Geldiniz!",
        "log_app_started": "[TR] --- Uygulama Başlatıldı ---",
        "log_app_closed": "[TR] --- Uygulama Kapatıldı ---",
        "log_greet_clicked": "[TR] Selamla butonuna tıklandı.",
        "log_dialog_cancelled": "[TR] İsim girişi kullanıcı tarafından iptal edildi.",
        "log_name_entered": "[TR] Girilen isim: {name}",
        "log_empty_name": "[TR] Kullanıcı boş isim ile onayladı.",
        "log_popup_closed": "[TR] '{name}' için açılan popup kapatıldı.",
        "log_anon_popup_closed": "[TR] Anonim popup penceresi kapatıldı.",
        "status_ready": "Sistem hazır.",
        "status_greeted": "Son işlem: {name} selamlandı.",
        "status_cancelled": "Son işlem: Giriş iptal edildi.",
        "status_error": "Hata oluştu: {error}",
        "lang_switch_tooltip": "Dili Değiştir / Switch Language",
    },
    Locale.EN: {
        "app_title": "Super Modern Popup App",
        "app_subtitle": "Lightweight, Secure & Responsive Greeting Experience",
        "btn_greet": "Greet",
        "btn_exit": "Exit",
        "btn_close": "Close",
        "btn_ok": "OK",
        "btn_cancel": "Cancel",
        "lang_toggle_btn": "🌐 EN ⇄ TR",
        "dialog_title": "Enter Name",
        "dialog_prompt": "Please enter your name:",
        "popup_title": "Greeting",
        "greeting_personalized": "Hello, {name}!",
        "greeting_anonymous": "Hello! Welcome to our Application!",
        "log_app_started": "[EN] --- Application Started ---",
        "log_app_closed": "[EN] --- Application Closed ---",
        "log_greet_clicked": "[EN] Greet button clicked.",
        "log_dialog_cancelled": "[EN] Name input cancelled by user.",
        "log_name_entered": "[EN] Entered name: {name}",
        "log_empty_name": "[EN] User confirmed with empty name.",
        "log_popup_closed": "[EN] Popup for '{name}' closed.",
        "log_anon_popup_closed": "[EN] Anonymous popup window closed.",
        "status_ready": "System ready.",
        "status_greeted": "Last action: {name} greeted.",
        "status_cancelled": "Last action: Input cancelled.",
        "status_error": "Error occurred: {error}",
        "lang_switch_tooltip": "Switch Language / Dili Değiştir",
    },
}


class I18nManager:
    """Manages active locale state and notifies listeners on language changes."""

    def __init__(self, default_locale: Locale = Locale.TR) -> None:
        self._current_locale: Locale = default_locale
        self._listeners: list[Callable[[Locale], None]] = []

    @property
    def current_locale(self) -> Locale:
        return self._current_locale

    def set_locale(self, locale: Locale | str) -> None:
        if isinstance(locale, str):
            locale = Locale(locale.lower())
        if locale != self._current_locale:
            self._current_locale = locale
            self._notify_listeners()

    def toggle_locale(self) -> Locale:
        new_locale = Locale.EN if self._current_locale == Locale.TR else Locale.TR
        self.set_locale(new_locale)
        return new_locale

    def add_listener(self, callback: Callable[[Locale], None]) -> None:
        if callback not in self._listeners:
            self._listeners.append(callback)

    def remove_listener(self, callback: Callable[[Locale], None]) -> None:
        if callback in self._listeners:
            self._listeners.remove(callback)

    def _notify_listeners(self) -> None:
        for callback in list(self._listeners):
            try:
                callback(self._current_locale)
            except Exception:
                pass

    def t(self, key: str, **kwargs: object) -> str:
        """Translate key for current locale with string formatting interpolation."""
        translations = MESSAGES.get(self._current_locale, MESSAGES[Locale.TR])
        text = translations.get(key, MESSAGES[Locale.TR].get(key, key))
        if kwargs:
            try:
                return text.format(**kwargs)
            except Exception:
                return text
        return text


# Global default i18n instance
I18N = I18nManager()
