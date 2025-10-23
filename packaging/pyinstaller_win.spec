# Bundle GUI with PySide6; run: pyinstaller --clean -y packaging/pyinstaller_win.spec
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hidden = collect_submodules("sudokutrainer") + collect_submodules("PySide6")
datas = collect_data_files("PySide6")

PROJECT_ROOT = os.path.abspath(os.getcwd())
ENTRY_SCRIPT = os.path.join(PROJECT_ROOT, "src", "sudokutrainer", "__main__.py")

block_cipher = None
a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=[],
    datas=datas,
    hiddenimports=hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
# Build a single-file executable by embedding binaries, zipfiles, and datas into EXE
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="SudokuTrainer",
    icon=None,
    console=False,
    upx=True,
)
