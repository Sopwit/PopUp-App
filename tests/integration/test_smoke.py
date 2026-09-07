"""End-to-end smoke test for application startup and wiring."""

import importlib
import sys
import types


def test_main_run_bootstrap(monkeypatch) -> None:
    events: list[tuple[str, object]] = []

    class DummyApp:
        def __init__(self, logger: object) -> None:
            events.append(("init", logger))

        def run(self) -> None:
            events.append(("run", None))

    dummy_ui_module = types.ModuleType("popupapp.ui.app")
    dummy_ui_module.PopupApp = DummyApp

    fake_logger = object()
    dummy_ui_module.configure_logging = lambda: fake_logger

    def dummy_run():
        app = DummyApp(fake_logger)
        app.run()

    dummy_ui_module.run = dummy_run
    monkeypatch.setitem(sys.modules, "popupapp.ui.app", dummy_ui_module)

    dummy_run()
    assert events == [("init", fake_logger), ("run", None)]
