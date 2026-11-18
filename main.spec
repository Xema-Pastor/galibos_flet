# -*- mode: python ; coding: utf-8 -*-
# Compilar con:  pyinstaller main.spec
# (no usar "pyinstaller --onefile main.py": regenera este fichero y se pierde la configuración)
import sys

sys.path.insert(0, SPECPATH)
from configuracion import VERSION

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],      # Logo e icono; Flet los busca en <_MEIPASS>/assets
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=f'PAGIF_v{VERSION}',
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
    icon='assets/icon.ico',
)
