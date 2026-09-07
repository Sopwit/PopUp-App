from pathlib import Path

project_dir = Path(SPECPATH).resolve().parents[1]
src_dir = project_dir / "src"

a = Analysis(
    [str(src_dir / "popupapp" / "__main__.py")],
    pathex=[str(src_dir)],
    binaries=[],
    datas=[
        (str(src_dir / "popupapp" / "assets"), "popupapp/assets"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='popupapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
