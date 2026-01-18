# 1. KRİTİK ADIM: Mimariyi zorla "linux/amd64" (Intel/AMD) yapıyoruz.
# Ubuntu 20.04 kullanıyoruz çünkü eski/yeni tüm Linuxlarda en iyi uyumluluğu sağlar.
FROM --platform=linux/amd64 ubuntu:20.04

# 2. Etkileşimli kurulumları engelle (Soru sormasın)
ENV DEBIAN_FRONTEND=noninteractive

# 3. Gerekli araçları yükle
# python3-tk: Pencere arayüzü için şart
# binutils: PyInstaller'ın exe yapması için gerekli araçlar
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    binutils \
    && rm -rf /var/lib/apt/lists/*

# 4. PyInstaller yükle (Uygulamayı tek dosya yapan araç)
RUN pip3 install pyinstaller

# 5. Çalışma klasörünü ayarla
WORKDIR /build

# 6. Senin kod dosyalarını içeri al
COPY . .

# 7. Derleme Komutu
# --onefile: Tek parça dosya olsun
# --windowed: Siyah konsol ekranı açılmasın
# --name popupapp: Çıkan dosyanın adı
# hidden-import: Bazen tkinter otomatik bulunamaz, elle ekliyoruz.
CMD pyinstaller --clean --onefile --windowed --hidden-import=tkinter --name popupapp popupapp.py && \
    mv dist/popupapp /output/
