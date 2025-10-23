# Bundle GUI with PySide6; run: pyinstaller --clean -y packaging/pyinstaller_win.spec
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hidden = collect_submodules("sudokutrainer") + collect_submodules("PySide6")
datas = collect_data_files("PySide6")

block_cipher = None
a = Analysis(
    ["src/sudokutrainer/__main__.py"],
    pathex=[],
    binaries=[],
    datas=datas,
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
