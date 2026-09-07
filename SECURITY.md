# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2.0 | :x:                |

## Reporting a Vulnerability

If you discover a potential security vulnerability within this project:
1. Please do not disclose it publicly on issues or forums.
2. Contact the maintainers directly with details and reproduction steps.
3. We will review and address the vulnerability promptly.

## Security Controls in PopUp-App
- **Input Sanitization**: User input is strictly sanitized with regex control-character elimination and max length enforcement to prevent Log Injection (CRLF / CWE-117).
- **Log Rotation**: Rotation limits prevent disk filling and Denial of Service.
- **Strict File Permissions**: Log directories are created with `0o700` POSIX permissions.
