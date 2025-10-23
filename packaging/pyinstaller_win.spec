# Minimal spec to bundle GUI; run: pyinstaller --clean -y packaging/pyinstaller_win.spec
from PyInstaller.utils.hooks import collect_submodules

hidden = collect_submodules("sudokutrainer")

block_cipher = None
a = Analysis(
    ["src/sudokutrainer/__main__.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SudokuTrainer",
    icon=None,
    console=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="SudokuTrainer",
)
