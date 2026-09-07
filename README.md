# PopUp App

**A secure, localized desktop greeting application built with Python and Tkinter.**

[![CI](https://github.com/Sopwit/PopUp-App/actions/workflows/ci.yml/badge.svg)](https://github.com/Sopwit/PopUp-App/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Sopwit/PopUp-App)](https://github.com/Sopwit/PopUp-App/releases)
[![License](https://img.shields.io/github/license/Sopwit/PopUp-App)](LICENSE)

---

## Overview

PopUp App provides a small, focused desktop flow: collect an optional name, display a localized greeting, and keep application diagnostics in an OS-appropriate rotating log. It is intentionally dependency-light at runtime and ships as portable Linux AppImages for both x86_64 and ARM64.

### Core capabilities

- **Localized desktop interface:** Turkish and English text can be switched while the application is running.
- **Safe greeting flow:** User input is normalized, limited, and stripped of control characters before it reaches logs or UI state.
- **Modal interaction:** The name prompt and greeting window retain focus correctly and clean up their modal ownership on close.
- **Portable Linux delivery:** GitHub Releases provide `.AppImage` artifacts for x86_64 and aarch64 systems.
- **Cross-platform verification:** The test matrix runs on Linux, macOS, and Windows; the Linux packaging job builds the AppImage artifact.

---

## Quick start

### Run from source

```bash
git clone https://github.com/Sopwit/PopUp-App.git
cd PopUp-App
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
make run
```

### Run the Linux AppImage

Download the artifact for your architecture from [GitHub Releases](https://github.com/Sopwit/PopUp-App/releases), then run:

```bash
chmod +x PopUp-App-<version>-<architecture>.AppImage
./PopUp-App-<version>-<architecture>.AppImage
```

Supported release architectures are `x86_64` and `aarch64`.

---

## Development commands

| Command | Purpose |
| --- | --- |
| `make run` | Run the application from the source tree. |
| `make test` | Run the complete pytest suite. |
| `make lint` | Compile the package and test sources. |
| `make check` | Run lint/compilation and tests together. |
| `make build` | Create a PyInstaller executable in `dist/`. |
| `APP_VERSION=<version> make appimage` | Build a Linux AppImage. |
| `make clean` | Remove local build and cache artifacts. |

---

## Documentation

- [Installation guide](docs/INSTALL.md) — source, AppImage, and environment requirements.
- [Build guide](docs/BUILD.md) — test, PyInstaller, AppImage, and container build workflows.
- [Architecture](docs/ARCHITECTURE.md) — package boundaries, UI flow, and lifecycle design.
- [Configuration reference](docs/CONFIGURATION.md) — constants, theme surface, localization, and log storage.
- [Security notes](docs/SECURITY.md) — input, logging, and reporting model.
- [Release guide](docs/RELEASE.md) — tag, artifact, integrity, and GitHub release process.
- [Change log](docs/CHANGELOG.md) — released and unreleased changes.
- [Türkçe özet](docs/overview/README.tr.md) — Turkish project overview.

## Project governance

- [Contributing guide](.github/CONTRIBUTING.md)
- [Code of conduct](.github/CODE_OF_CONDUCT.md)
- [Security policy](.github/SECURITY.md)

## License

PopUp App is released under the [MIT License](LICENSE).
