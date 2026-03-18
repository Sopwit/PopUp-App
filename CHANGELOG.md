# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog,
and this project follows Semantic Versioning.

## [Unreleased]

### Added

- Cross-platform CI matrix for Linux, macOS, and Windows.
- Linux packaging flow with PyInstaller.
- Bilingual documentation (`README.md`, `README_TR.md`).

### Changed

- Project refactored into modular `app/` package structure.
- Logging setup improved for cross-platform paths and handler reuse.

### Removed

- Legacy `requirements-dev.txt` in favor of `install.txt` and `dev-install.txt`.

## [0.1.0] - 2026-03-18

### Added

- Initial popup desktop app with Tkinter.
