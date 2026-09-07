"""Shared pytest fixtures and test configuration."""

import logging
import tkinter as tk
from typing import Generator
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tk_root() -> Generator[tk.Tk, None, None]:
    """Provide an isolated, withdrawn Tkinter root instance."""
    root = tk.Tk()
    root.withdraw()
    yield root
    try:
        root.destroy()
    except Exception:
        pass


@pytest.fixture
def mock_logger() -> MagicMock:
    """Provide a mock logger instance for assertions."""
    return MagicMock(spec=logging.Logger)
