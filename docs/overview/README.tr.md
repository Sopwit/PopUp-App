# PopUp App

**Python ve Tkinter ile geliştirilmiş, güvenli ve iki dilli masaüstü karşılama uygulaması.**

## Genel bakış

PopUp App, isteğe bağlı bir isim alır, kullanıcıyı Türkçe veya İngilizce karşılar ve uygulama tanı kayıtlarını işletim sistemine uygun dönen log dosyalarında saklar. Linux için taşınabilir AppImage dosyaları x86_64 ve ARM64 mimarilerinde yayınlanır.

## Hızlı başlangıç

```bash
git clone https://github.com/Sopwit/PopUp-App.git
cd PopUp-App
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
make run
```

AppImage kullanmak için [GitHub Releases](https://github.com/Sopwit/PopUp-App/releases) sayfasından mimarinize uygun dosyayı indirin:

```bash
chmod +x PopUp-App-<version>-<architecture>.AppImage
./PopUp-App-<version>-<architecture>.AppImage
```

## Belgeler

- [Ana README](../../README.md)
- [Kurulum](../INSTALL.md)
- [Derleme](../BUILD.md)
- [Mimari](../ARCHITECTURE.md)
- [Yapılandırma](../CONFIGURATION.md)
- [Güvenlik](../SECURITY.md)
- [Yayın süreci](../RELEASE.md)

## Temel özellikler

- Çalışma anında Türkçe/İngilizce dil değişimi.
- Kontrol karakterlerini temizleyen güvenli isim girişi.
- Modal giriş ve karşılama pencereleri.
- Platforma uygun, boyutu sınırlı dönen log dosyaları.
- x86_64 ve aarch64 Linux AppImage yayınları.
