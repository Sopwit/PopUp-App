# Configuration reference

PopUp App has no external configuration file. Its runtime behavior is defined by package constants and the active locale state.

## Application constants

| Constant | Value | Purpose |
| --- | --- | --- |
| `APP_NAME` | `super_popup_app` | Logger and platform data-directory name. |
| `MAX_NAME_LENGTH` | `50` | Maximum sanitized greeting-name length. |
| `MAX_LOG_BYTES` | `1_048_576` | Maximum active log-file size before rotation. |
| `BACKUP_COUNT` | `3` | Number of rotated log backups retained. |
| `DEFAULT_DIR_PERMISSIONS` | `0o700` | POSIX permission mode for created log directories. |
| `MAIN_WINDOW_WIDTH` / `HEIGHT` | `520` / `265` | Main-window geometry. |
| `POPUP_WINDOW_WIDTH` / `HEIGHT` | `360` / `190` | Greeting-modal geometry. |

## Locale behavior

`Locale.TR` is the default locale; `Locale.EN` is available through the language button. `I18nManager` keeps a listener list so widgets update when the active locale changes. Translation strings live in `src/popupapp/i18n/translations.py` and both catalogs are covered by tests for key parity.

## Theme behavior

`UITheme` is an immutable dataclass in `src/popupapp/config/theme.py`. It owns palette values, typography, action colors, and hover colors. Keep new UI colors and fonts in this class rather than adding widget-local literals.

## Logging behavior

`configure_logging()` creates or reuses a named `RotatingFileHandler`. Reconfiguration does not duplicate handlers and closes handlers targeting outdated log paths. User text is sanitized before it is interpolated into log messages.

## Packaged assets

The application icon is stored at `src/popupapp/assets/popupapp.png` and loaded via `importlib.resources`. Do not depend on the caller’s current working directory for packaged assets.
