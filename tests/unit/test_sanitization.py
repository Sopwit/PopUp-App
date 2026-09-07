"""Unit tests for string sanitization and CRLF log injection defense."""

import pytest
from popupapp.core.sanitization import sanitize_input


@pytest.mark.parametrize(
    ("raw_input", "expected"),
    [
        (None, ""),
        ("", ""),
        ("   ", ""),
        ("Emir", "Emir"),
        ("  John Doe  ", "John Doe"),
        ("Hello    World    From   Tkinter", "Hello World From Tkinter"),
    ],
)
def test_sanitize_input_normalization(raw_input: str | None, expected: str) -> None:
    assert sanitize_input(raw_input) == expected


def test_sanitize_input_neutralizes_crlf_injection() -> None:
    malicious = "Admin\n2026-09-07 - CRITICAL - Forged Log Entry\r\nAnother Line"
    cleaned = sanitize_input(malicious, max_length=100)
    assert "\n" not in cleaned
    assert "\r" not in cleaned
    assert cleaned == "Admin 2026-09-07 - CRITICAL - Forged Log Entry Another Line"


def test_sanitize_input_strips_control_and_null_bytes() -> None:
    text_with_controls = "User\x00\x07\x08\x1b\x7f\x80Security"
    cleaned = sanitize_input(text_with_controls)
    assert "\x00" not in cleaned
    assert "\x07" not in cleaned
    assert "\x08" not in cleaned
    assert "\x1b" not in cleaned
    assert cleaned == "User Security"


def test_sanitize_input_truncates_at_boundary() -> None:
    long_name = "X" * 120
    cleaned = sanitize_input(long_name, max_length=50)
    assert len(cleaned) == 50
    assert cleaned == "X" * 50
