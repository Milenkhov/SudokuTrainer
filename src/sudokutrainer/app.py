from __future__ import annotations

import os
import sys

from PySide6.QtWidgets import QApplication

from .gui.main_window import MainWindow


def main(argv: list[str] | None = None) -> int:
    # Headless-friendly for CI/tests
    if os.environ.get("CI") and not os.environ.get("QT_QPA_PLATFORM"):
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = QApplication(sys.argv if argv is None else argv)
    app.setApplicationName("SudokuTrainer")
    app.setOrganizationName("Milenkhov")
    win = MainWindow()
    win.show()
    return app.exec()
