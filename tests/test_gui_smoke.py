import os

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


@pytest.mark.parametrize("offscreen", [True])
def test_main_window_smoke(offscreen):
    try:
        from PySide6.QtWidgets import QApplication

        from sudokutrainer.gui.main_window import MainWindow
    except Exception as exc:
        pytest.skip(f"PySide6 unavailable: {exc}")

    QApplication([])
    win = MainWindow()
    assert win.windowTitle()
    win.close()
