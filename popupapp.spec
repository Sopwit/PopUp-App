# -*- mode: python ; coding: utf-8 -*-
import os
import sys

spec_dir = os.path.abspath(SPECPATH)
src_dir = os.path.join(spec_dir, "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

block_cipher = None

a = Analysis(
    [os.path.join(src_dir, 'popupapp', '__main__.py')],
    pathex=[src_dir],
    binaries=[],
    datas=[
        (os.path.join(spec_dir, 'logo.png'), '.'),
    ],
    hiddenimports=['tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['unittest', 'pdb', 'difflib', 'doctest', 'email', 'html', 'http', 'xml'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

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
