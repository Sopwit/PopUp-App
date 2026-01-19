# 🌟 Super Modern Popup App

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge)

**Super Modern Popup App**, kullanıcı etkileşimli, şık arayüzlü ve gelişmiş loglama özelliklerine sahip bir Python masaüstü uygulamasıdır. `Tkinter` kütüphanesi kullanılarak geliştirilmiş olup, modern tasarım prensipleri ve kullanıcı dostu bir deneyim sunar.

## 🚀 Özellikler

- **🎨 Modern Arayüz**: Koyu mod temalı, göz yormayan şık tasarım.
- **✨ Etkileşimli Deneyim**: Kullanıcıdan isim alarak kişiselleştirilmiş karşılama mesajları.
- **📝 Detaylı Loglama**: Tüm kullanıcı etkileşimleri ve sistem hataları otomatik olarak kaydedilir.
- **💫 Hover Efektleri**: Butonlar üzerinde akıcı görsel geri bildirimler.
- **🔒 Hata Yönetimi**: Beklenmedik durumlara karşı güvenli hata yakalama mekanizması.

## 🛠️ Gereksinimler

Projenin çalışması için aşağıdakilerin sisteminizde yüklü olması gerekir:

- **Python 3.x**: [Python İndir](https://www.python.org/downloads/)
- **Tkinter**: Python ile birlikte gelir (Linux kullanıcıları için: `sudo apt-get install python3-tk`)

## 📥 Kurulum

Proje dosyalarını yerel makinenize klonlayın:

```bash
git clone https://github.com/Sopwit/popup-app.git
cd popup-app
```

## ▶️ Kullanım

### Normal Çalıştırma

Terminal veya komut satırı üzerinden uygulamayı başlatın:

```bash
python3 popupapp.py
```

### Docker ile Çalıştırma

Uygulamayı izole bir ortamda çalıştırmak isterseniz Docker kullanabilirsiniz:

1. **Docker İmajını Oluşturun:**

   ```bash
   docker build -t popup-app .
   ```

2. **Konteyneri Başlatın:**
   _(Not: GUI uygulamalarını Docker üzerinde çalıştırmak için X11 yönlendirmesi gibi ek yapılandırmalar gerekir.)_

## 📂 Proje Yapısı

```
PopUp-App/
├── popupapp.py      # Ana uygulama dosyası ve kaynak kodlar
├── Dockerfile       # Docker yapılandırma dosyası
├── LICENSE          # MIT Lisans dosyası
├── README.md        # Proje dokümantasyonu
└── logo.png         # Uygulama logosu
```

## 📝 Loglama

Uygulama logları işletim sisteminize göre aşağıdaki dizinde, `app_log.txt` dosyasında saklanır:

- **Linux/macOS**: `~/.local/share/super_popup_app/`
- **Dosya Yolu**: `~/.local/share/super_popup_app/app_log.txt`

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir "Pull Request" göndermeden önce mevcut kod yapısını inceleyin ve değişikliklerinizi test edin.

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.
