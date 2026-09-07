# Installation

## Supported environments

| Environment | Status | Delivery method |
| --- | --- | --- |
| Linux x86_64 | Supported | AppImage or source. |
| Linux ARM64 / aarch64 | Supported | AppImage or source. |
| macOS | Source execution verified in CI. | Source. |
| Windows | Source execution verified in CI. | Source. |

Tkinter must be available in the Python installation used for source execution. On Debian/Ubuntu, install `python3-tk`; on Fedora, install `python3-tkinter`.

## Portable Linux AppImage

1. Open [GitHub Releases](https://github.com/Sopwit/PopUp-App/releases).
2. Download the `.AppImage` matching `x86_64` or `aarch64`.
3. Mark it executable and launch it.

```bash
chmod +x PopUp-App-<version>-<architecture>.AppImage
./PopUp-App-<version>-<architecture>.AppImage
```

The AppImage is self-contained and does not install files system-wide.

## Source installation

```bash
git clone https://github.com/Sopwit/PopUp-App.git
cd PopUp-App
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
make run
```

For a runtime-only package installation, use:

```bash
python -m pip install .
popupapp
```

## Logs

The application stores its rotating log under the current user’s platform data directory:

| Platform | Location |
| --- | --- |
| Linux | `~/.local/share/super_popup_app/app_log.txt` |
| macOS | `~/Library/Application Support/super_popup_app/app_log.txt` |
| Windows | `%APPDATA%\super_popup_app\app_log.txt` |

See [Configuration](CONFIGURATION.md) for log retention settings.
