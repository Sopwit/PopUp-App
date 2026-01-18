# Super Modern Popup App 🌟

Modern, kullanıcı etkileşimli ve loglama özelliklerine sahip basit bir Python Tkinter uygulaması.

## Özellikler

- **Modern Arayüz**: Temiz ve şık tasarım.
- **Etkileşimli**: Kullanıcıdan isim alarak kişiselleştirilmiş karşılama mesajları gösterir.
- **Loglama**: Tüm işlemleri ve hataları `~/.local/share/super_popup_app/app_log.txt` dosyasına kaydeder.
- **Hover Efektleri**: Butonlar üzerinde görsel geri bildirimler.

## Gereksinimler

- Python 3.x
- Tkinter (Python ile birlikte gelir, Linux'ta `sudo apt-get install python3-tk` gerekebilir)

## Kurulum ve Çalıştırma

1. Repoyu klonlayın:

   ```bash
   git clone https://github.com/Sopwit/popup-app.git
   cd popup-app
   ```

2. Uygulamayı çalıştırın:
   ```bash
   python3 popupapp.py
   ```

## Docker ile Çalıştırma

Uygulama Docker desteği ile gelmektedir. Dockerfile kullanarak imaj oluşturabilirsiniz:

```bash
docker build -t popup-app .
# GUI uygulamalarını Docker ile çalıştırmak ek yapılandırma gerektirir.
```

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
