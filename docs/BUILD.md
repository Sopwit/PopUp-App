# Build and Packaging Guide

## Prerequisites

- Python 3.10 or higher
- `pip` and virtual environment support
- Tkinter library installed (e.g. `python3-tk` on Debian/Ubuntu, `python3-tkinter` on Fedora)

## Local Standalone Binary Build

PopUp-App uses PyInstaller with a customized `popupapp.spec` for single-file cross-platform binaries:

```bash
make dev-install
make build
```

The output binary will be located at `dist/popupapp` (`dist/popupapp.exe` on Windows).

## Dockerized Linux Build

You can generate reproducible Linux binaries using Docker:

```bash
docker build -t popup-builder .
docker run --rm -v "$(pwd)/output:/output" popup-builder
```

Output: `output/popupapp-linux`
