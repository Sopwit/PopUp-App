# Contributing

## Development setup

```bash
git clone https://github.com/Sopwit/PopUp-App.git
cd PopUp-App
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
make check
```

## Change expectations

- Keep application code under `src/popupapp/` and tests under `tests/`.
- Add or update tests for observable behavior changes.
- Keep translations key-complete across Turkish and English catalogs.
- Keep UI state modal-safe and avoid workdir-dependent asset paths.
- Run `make check` before opening a pull request.

## Pull requests

Describe the user-visible change, testing performed, and any release or packaging impact. Keep unrelated refactors out of the same pull request.
