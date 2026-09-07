"""Domain logic for input validation, sanitization and security defenses."""

import re
from popupapp.config.constants import MAX_NAME_LENGTH

# Matches carriage return, newline, tabs, and non-printable control chars (ASCII 0-31 and 127-159)
_CONTROL_CHAR_REGEX = re.compile(r"[\r\n\t\x00-\x1f\x7f-\x9f]")


def sanitize_input(text: str | None, max_length: int = MAX_NAME_LENGTH) -> str:
    """Sanitize user input to neutralize Log Injection (CRLF injection) and layout anomalies.

    Args:
        text: Raw user input from dialog or external source.
        max_length: Maximum allowed string length after sanitization.

    Returns:
        Cleaned, single-line sanitized string.
    """
    if not text:
        return ""

    # Replace all control characters with standard whitespace
    cleaned = _CONTROL_CHAR_REGEX.sub(" ", text)

    # Normalize internal whitespaces and collapse multiple spaces
    cleaned = " ".join(cleaned.split())

    # Enforce strict length boundaries
    return cleaned[:max_length].strip()
