import importlib
import sys
import types


def test_main_run_wires_logger_and_app(monkeypatch) -> None:
    events: list[tuple[str, object]] = []

    class DummyApp:
        def __init__(self, logger: object) -> None:
            events.append(("init", logger))

        def run(self) -> None:
            events.append(("run", None))

    dummy_ui_module = types.ModuleType("app.ui.popup_ui")
    dummy_ui_module.PopupApp = DummyApp
    monkeypatch.setitem(sys.modules, "app.ui.popup_ui", dummy_ui_module)

    sys.modules.pop("app.main", None)
    main = importlib.import_module("app.main")

    fake_logger = object()
    monkeypatch.setattr(main, "configure_logging", lambda: fake_logger)

    main.run()

    assert events == [("init", fake_logger), ("run", None)]
