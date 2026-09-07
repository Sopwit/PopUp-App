#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
version="${APP_VERSION:?Set APP_VERSION to the release version (for example 0.1.0).}"
architecture="${ARCH:-x86_64}"
appimagetool=("${APPIMAGETOOL:-appimagetool}")
if [[ "${APPIMAGETOOL_EXTRACT_AND_RUN:-0}" == "1" ]]; then
    appimagetool+=(--appimage-extract-and-run)
fi
app_dir="${project_root}/build/AppDir"
output_dir="${project_root}/dist"
binary="${project_root}/dist/popupapp"

if [[ ! -x "${binary}" ]]; then
    echo "Missing PyInstaller binary: ${binary}. Run make build first." >&2
    exit 1
fi

rm -rf "${app_dir}"
mkdir -p "${app_dir}/usr/bin" "${app_dir}/usr/share/applications" \
    "${app_dir}/usr/share/icons/hicolor/256x256/apps" "${app_dir}/usr/share/metainfo"

install -m 0755 "${binary}" "${app_dir}/usr/bin/popupapp"
install -m 0644 "${project_root}/packaging/appimage/io.github.Sopwit.PopUpApp.desktop" \
    "${app_dir}/usr/share/applications/io.github.Sopwit.PopUpApp.desktop"
install -m 0644 "${project_root}/src/popupapp/assets/popupapp.png" \
    "${app_dir}/usr/share/icons/hicolor/256x256/apps/io.github.Sopwit.PopUpApp.png"
install -m 0644 "${project_root}/packaging/appimage/io.github.Sopwit.PopUpApp.appdata.xml" \
    "${app_dir}/usr/share/metainfo/io.github.Sopwit.PopUpApp.appdata.xml"
ln -s usr/share/applications/io.github.Sopwit.PopUpApp.desktop \
    "${app_dir}/io.github.Sopwit.PopUpApp.desktop"
ln -s usr/share/icons/hicolor/256x256/apps/io.github.Sopwit.PopUpApp.png \
    "${app_dir}/io.github.Sopwit.PopUpApp.png"

mkdir -p "${output_dir}"
ARCH="${architecture}" "${appimagetool[@]}" "${app_dir}" \
    "${output_dir}/PopUp-App-${version}-${architecture}.AppImage"
