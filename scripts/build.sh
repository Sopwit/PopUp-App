#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

echo "📦 Packaging single-file binary with PyInstaller..."
pyinstaller --clean popupapp.spec
echo "✅ Build completed: ${ROOT_DIR}/dist/popupapp"
