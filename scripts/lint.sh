#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

echo "🔍 Running compilation and syntax checks..."
python3 -m compileall src/ tests/ popupapp.py
echo "✅ All Python files passed syntax validation."
