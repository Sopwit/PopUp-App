# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog,
and this project follows Semantic Versioning.

## [0.0.1] - 2026-09-07

### Added
- **Production Desktop Architecture**: Clean layered package (`src/popupapp/`) featuring presentation, domain, and infrastructure separation.
- **Dynamic Localization (i18n)**: Runtime toggleable Turkish (`TR`) and English (`EN`) language support via a sleek `🌐 TR` / `🌐 EN` header icon.
- **Modern Dark UI**: Jitter-free, elevated card design with custom color palette and responsive hover feedback.
- **Security Hardening**:
  - Input sanitization against Log Injection (CWE-117 / CRLF injection).
  - Rotating file logger (1MB limit, 3 backups) to prevent disk exhaustion.
  - Secure directory creation mode (`0o700`).
- **Modal Window Management**: Ebeveyn pencere merkezleme, transient ilişkilendirme ve klavye kısayolları.
- **Packaging & DevOps**: Multi-OS GitHub Actions CI/CD, PyInstaller standalone binary packaging, and complete test suite (31/31 tests).
