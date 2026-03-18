from app.services.logging_setup import configure_logging
from app.ui.popup_ui import PopupApp


def run() -> None:
    logger = configure_logging()
    app = PopupApp(logger)
    app.run()


if __name__ == "__main__":
    run()
