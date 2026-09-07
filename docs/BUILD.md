# Build and Packaging Guide

## Prerequisites

- Python 3.10 or higher
- `pip` and virtual environment support
- Tkinter library installed (e.g. `python3-tk` on Debian/Ubuntu, `python3-tkinter` on Fedora)

## Local Standalone Binary Build

PopUp-App uses the PyInstaller specification at `packaging/pyinstaller/popupapp.spec` for single-file cross-platform binaries:

```bash
make dev-install
make build
```

The output binary will be located at `dist/popupapp` (`dist/popupapp.exe` on Windows).

## Linux AppImage

Install `appimagetool`, then build a portable Linux package:

```bash
APP_VERSION=0.1.0 make appimage
```

The output is `dist/PopUp-App-0.1.0-x86_64.AppImage`. The package includes standard desktop-entry and AppStream metadata.

## Dockerized Linux Build

You can generate reproducible Linux binaries using Docker:

```bash
docker build -f docker/Dockerfile -t popup-builder .
docker run --rm -v "$(pwd)/output:/output" popup-builder
```

Output: `output/popupapp-linux`
