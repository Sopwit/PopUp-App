# Super Modern Popup App

Tkinter ile yazilmis kucuk bir masaustu popup uygulamasi.

## Ozellikler

- Basit ve modern arayuz
- Isim bazli popup karsilama mesaji
- Uygulama ve popup etkileşimleri icin dosya loglama
- Linux, macOS ve Windows icin uygun log dizini secimi

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
│   └── test_logging_setup.py
├── .github/workflows/ci.yml
├── popupapp.py
├── Dockerfile
├── requirements-dev.txt
└── README.md
```

## Gereksinimler

- Python 3.10+
- Tkinter (Linux'ta gerekirse `python3-tk` paketi)

## Yerel Calistirma

```bash
python3 popupapp.py
```

## Test

```bash
python3 -m pip install -r requirements-dev.txt
pytest -q
```

## Docker ile Linux Binary Uretimi

```bash
docker build -t popup-app-builder .
docker run --rm -v "$PWD/output:/output" popup-app-builder
```

Uretilen dosya: `output/popupapp-linux`

## Log Dosyasi Konumu

- Linux: `~/.local/share/super_popup_app/app_log.txt`
- macOS: `~/Library/Application Support/super_popup_app/app_log.txt`
- Windows: `%APPDATA%\super_popup_app\app_log.txt`

## CI

GitHub Actions workflow'u her push ve pull request'te:

- Kodun import/syntax kontrolunu yapar
- `pytest` testlerini calistirir
- `ubuntu-latest`, `macos-latest` ve `windows-latest` uzerinde dogrulama yapar

## Lisans

MIT (`LICENSE`)
