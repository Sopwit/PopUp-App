import logging

from app.services.logging_setup import APP_NAME, LOG_FILE_NAME, configure_logging, resolve_log_dir


def test_resolve_log_dir_linux() -> None:
    result = resolve_log_dir(platform_name="linux", home_dir="/home/test")
    assert str(result) == "/home/test/.local/share/super_popup_app"


def test_resolve_log_dir_macos() -> None:
    result = resolve_log_dir(platform_name="darwin", home_dir="/Users/test")
    assert str(result) == "/Users/test/Library/Application Support/super_popup_app"


def test_resolve_log_dir_windows_with_appdata() -> None:
    result = resolve_log_dir(
        platform_name="win32",
        home_dir="C:/Users/test",
        appdata_dir="C:/Users/test/AppData/Roaming",
    )
    assert str(result).replace("\\", "/") == "C:/Users/test/AppData/Roaming/super_popup_app"


def test_resolve_log_dir_windows_without_appdata() -> None:
    result = resolve_log_dir(platform_name="win32", home_dir="C:/Users/test", appdata_dir="")
    assert str(result).replace("\\", "/") == "C:/Users/test/AppData/Roaming/super_popup_app"


def test_resolve_log_dir_windows_uses_env_appdata_when_param_is_none(monkeypatch) -> None:
    monkeypatch.setenv("APPDATA", "C:/Env/AppData/Roaming")
    result = resolve_log_dir(platform_name="win32", home_dir="C:/Users/test", appdata_dir=None)
    assert str(result).replace("\\", "/") == "C:/Env/AppData/Roaming/super_popup_app"


def test_resolve_log_dir_unknown_platform_defaults_to_local_share() -> None:
    result = resolve_log_dir(platform_name="freebsd", home_dir="/home/test")
    assert str(result) == "/home/test/.local/share/super_popup_app"


def test_configure_logging_reuses_handler_and_writes_log(monkeypatch, tmp_path) -> None:
    logger = logging.getLogger(APP_NAME)
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()

    monkeypatch.setattr("app.services.logging_setup.resolve_log_dir", lambda: tmp_path)

    first_logger = configure_logging()
    second_logger = configure_logging()

    file_handlers = [h for h in first_logger.handlers if isinstance(h, logging.FileHandler)]
    assert first_logger is second_logger
    assert len(file_handlers) == 1
    assert (tmp_path / LOG_FILE_NAME).exists()

    for handler in list(first_logger.handlers):
        first_logger.removeHandler(handler)
        handler.close()
