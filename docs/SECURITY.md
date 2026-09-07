# Security architecture

## Scope

PopUp App is a local desktop utility. It does not accept network requests, manage credentials, or execute user-provided code. Its security boundary is the local GUI input and local diagnostic log.

## Input and log integrity

Name input passes through `sanitize_input()` before it is logged or used in a greeting. The sanitizer:

- Removes carriage returns, line feeds, tabs, null bytes, and other ASCII control characters.
- Collapses repeated whitespace into one space.
- Enforces the configured maximum length.

This prevents control-character and CRLF log injection (CWE-117) through the greeting field.

## Log availability and permissions

- Logs use `RotatingFileHandler` with a 1 MiB active-file limit and three backups.
- New POSIX log directories are created with `0o700` permissions.
- Platform-aware paths avoid writing application logs to the project checkout.

## Packaging trust boundary

Release AppImages are produced from version tags by GitHub Actions. Verify the SHA-256 digest published in the corresponding GitHub Release before running a downloaded artifact.

## Reporting vulnerabilities

Do not disclose suspected vulnerabilities through public issues. Report a concise reproduction, impact assessment, affected version, and any mitigations directly to the repository maintainers through GitHub’s private security reporting channel when available.
