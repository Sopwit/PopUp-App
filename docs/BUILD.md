# Build and development

## Prerequisites

- Python 3.10 or newer.
- Tkinter headers/runtime for GUI execution.
- A virtual environment is recommended.
- `PyInstaller` is installed through the `dev` dependency group.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
```

## Quality gate

Run the full local verification gate before publishing a change:

```bash
make check
```

It compiles `src/` and `tests/`, then executes the pytest suite. Linux GUI tests use `xvfb-run` in GitHub Actions; local tests skip display-dependent fixtures when no display is available.

## PyInstaller executable

```bash
make build
```

The executable is produced at `dist/popupapp`. The packaging definition is `packaging/pyinstaller/popupapp.spec`; application assets are included from `src/popupapp/assets/`.

## AppImage

Install `appimagetool` for the local architecture, then run:

```bash
APP_VERSION=0.1.0 make appimage
```

The output is `dist/PopUp-App-0.1.0-<architecture>.AppImage`. The builder validates the desktop entry and includes AppStream metadata, application icon, and PyInstaller executable.

## Containerized Linux build

```bash
docker build -f docker/Dockerfile -t popupapp-builder .
docker run --rm -v "$(pwd)/output:/output" popupapp-builder
```

The container creates a Linux PyInstaller executable in the mounted `output/` directory. Use the AppImage path for portable release assets.

## CI matrix

GitHub Actions runs tests on Linux, macOS, and Windows. After the test matrix succeeds, the Linux package job produces an AppImage artifact. The release workflow attaches matching `.AppImage` assets to a version tag.
