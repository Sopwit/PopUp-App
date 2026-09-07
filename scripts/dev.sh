#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="${ROOT_DIR}/src:${ROOT_DIR}"

echo "🚀 Starting Super Modern Popup App in dev mode..."
python3 "${ROOT_DIR}/popupapp.py" "$@"
