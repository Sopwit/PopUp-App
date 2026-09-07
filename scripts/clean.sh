#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

echo "🧹 Cleaning temporary files and build artifacts..."
rm -rf build/ dist/ __pycache__ .pytest_cache/ *.egg-info .eggs/ output/
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
echo "✨ Workspace clean."
