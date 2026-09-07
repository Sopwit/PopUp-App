# Security Architecture & Controls

## Threat Modeling & Mitigations

### 1. Log Injection / CRLF Manipulation (CWE-117)
- **Vulnerability**: Unsanitized user string input containing carriage returns (`\r`) or line feeds (`\n`) can craft deceptive log lines or corrupt log parsers.
- **Mitigation**: `popupapp.core.sanitization.sanitize_input()` removes all ASCII control characters (`0x00`-`0x1F` and `0x7F`-`0x9F`) and enforces a 50-character limit before logging.

### 2. Disk Exhaustion (Denial of Service)
- **Vulnerability**: Unbounded logging in standard `FileHandler` can consume arbitrary disk space.
- **Mitigation**: Configured `RotatingFileHandler` with strict 1MB byte limit (`maxBytes=1_048_576`) and max 3 rollover backups (`backupCount=3`).

### 3. File System Permissions
- **Mitigation**: Storage directories are initialized with POSIX `0o700` permissions (`rwx------`), restricting read/write access to the current system user.
