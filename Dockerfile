FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

RUN apt-get update && apt-get install -y \
    python3-tk \
    binutils \
    && rm -rf /var/lib/apt/lists/*

COPY dev-install.txt ./
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r dev-install.txt

COPY . .

# Linux icin tek dosya binary uretilir.
CMD pyinstaller --clean --onefile --windowed --hidden-import=tkinter --name popupapp popupapp.py && \
    mkdir -p /output && \
    cp dist/popupapp /output/popupapp-linux
