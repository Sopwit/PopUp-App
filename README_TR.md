# Super Modern Popup App

Tkinter ile gelistirilmis hafif bir masaustu popup uygulamasi.

English documentation: [README.md](README.md)

## Ozellikler

- Sade ve modern arayuz
- Isme ozel karsilama popup'i
- Uygulama ve popup etkilesimleri icin dosya loglama
- Linux, macOS ve Windows icin platforma uygun log dizini secimi

## Proje Yapisi

```text
PopUp-App/
├── app/
│   ├── main.py
│   ├── services/
│   │   └── logging_setup.py
│   └── ui/
│       └── popup_ui.py
├── tests/
│   ├── test_logging_setup.py
│   └── test_smoke.py
├── .github/workflows/ci.yml
├── .github/workflows/release.yml
├── .github/RELEASE_TEMPLATE.md
├── .github/release.yml
├── popupapp.py
├── Dockerfile
├── install.txt
├── dev-install.txt
├── CHANGELOG.md
├── README.md
└── README_TR.md
```

## Gereksinimler

- Python 3.10+
- Tkinter (Linux'ta gerekirse `python3-tk`)

Runtime bagimliliklarini kurma:

```bash
python3 -m pip install -r install.txt
```

## Yerel Calistirma

```bash
python3 popupapp.py
```

## Test

```bash
python3 -m pip install -r dev-install.txt
pytest -q
```

## Docker ile Linux Binary Uretimi

```bash
docker build -t popup-app-builder .
docker run --rm -v "$PWD/output:/output" popup-app-builder
```

Uretilen dosya: `output/popupapp-linux`

## Log Dosyasi Konumlari

- Linux: `~/.local/share/super_popup_app/app_log.txt`
- macOS: `~/Library/Application Support/super_popup_app/app_log.txt`
- Windows: `%APPDATA%\\super_popup_app\\app_log.txt`

## CI

GitHub Actions workflow'u her push ve pull request'te:

- syntax/import kontrollerini yapar
- `pytest` testlerini calistirir
- `ubuntu-latest`, `macos-latest` ve `windows-latest` uzerinde dogrular
- PyInstaller ile Linux binary uretir
- `popupapp-linux` artifact olarak yukler

## Release

- Tag formati: `vMAJOR.MINOR.PATCH` (ornek: `v0.1.0`)
- Release workflow: [`.github/workflows/release.yml`](.github/workflows/release.yml)
- Release template: [`.github/RELEASE_TEMPLATE.md`](.github/RELEASE_TEMPLATE.md)
- Changelog kaynagi: [`CHANGELOG.md`](CHANGELOG.md)

Tag olusturma ve push:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Lisans

MIT (`LICENSE`)
