FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

RUN apt-get update && apt-get install -y \
    python3-tk \
    binutils \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir ".[dev]"

# Linux icin tek dosya binary uretilir.
CMD pyinstaller packaging/pyinstaller/popupapp.spec && \
    mkdir -p /output && \
    cp dist/popupapp /output/popupapp-linux
