from app.services.logging_setup import resolve_log_dir


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
