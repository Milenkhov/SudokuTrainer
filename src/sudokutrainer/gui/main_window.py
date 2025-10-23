from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from ..services.game_service import GameService
from .board_widget import BoardWidget
from .theming import STYLE_DARK, STYLE_LIGHT


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SudokuTrainer")
        self.service = GameService()
        self._build_ui()
        self._apply_theme("light")
        self._new_puzzle()

    def _build_ui(self) -> None:
        # Toolbar
        tb = QToolBar("Main")
        self.addToolBar(tb)

        self.level_combo = QComboBox()
        self.level_combo.addItems(["Beginner", "Easy", "Medium", "Hard", "Expert"])
        self.level_combo.setCurrentText(self.service.level)
        self.level_combo.currentTextChanged.connect(self._on_level_changed)  # type: ignore[attr-defined]
        tb.addWidget(QLabel("Level: "))
        tb.addWidget(self.level_combo)

        btn_new = QPushButton("New")
        btn_new.clicked.connect(self._new_puzzle)  # type: ignore[attr-defined]
        tb.addWidget(btn_new)

        btn_hint = QPushButton("Hint")
        btn_hint.clicked.connect(self._hint)  # type: ignore[attr-defined]
        tb.addWidget(btn_hint)

        btn_solve = QPushButton("Solve")
        btn_solve.clicked.connect(self._solve)  # type: ignore[attr-defined]
        tb.addWidget(btn_solve)

        btn_theme = QPushButton("Toggle Theme")
        btn_theme.clicked.connect(self._toggle_theme)  # type: ignore[attr-defined]
        tb.addWidget(btn_theme)

        # Central layout
        central = QWidget()
        lay = QHBoxLayout(central)
        self.board_widget = BoardWidget()
        self.board_widget.cellEdited.connect(self._on_cell_edited)  # type: ignore[attr-defined]
        lay.addWidget(self.board_widget, 1)

        side = QWidget()
        side_lay = QVBoxLayout(side)
        self.status_info = QLabel("")
        side_lay.addWidget(self.status_info)
        side_lay.addStretch(1)
        lay.addWidget(side, 0)

        self.setCentralWidget(central)
        self.setStatusBar(QStatusBar())

        # Menus
        file_menu = self.menuBar().addMenu("&File")
        act_open = file_menu.addAction("Open…")
        act_open.triggered.connect(self._open)  # type: ignore[attr-defined]
        act_save = file_menu.addAction("Save")
        act_save.triggered.connect(self._save)  # type: ignore[attr-defined]
        file_menu.addSeparator()
        act_exit = file_menu.addAction("Exit")
        act_exit.triggered.connect(self.close)  # type: ignore[attr-defined]

        edit_menu = self.menuBar().addMenu("&Edit")
        act_undo = edit_menu.addAction("Undo")
        act_undo.triggered.connect(self._undo)  # type: ignore[attr-defined]
        act_redo = edit_menu.addAction("Redo")
        act_redo.triggered.connect(self._redo)  # type: ignore[attr-defined]

        game_menu = self.menuBar().addMenu("&Game")
        act_hint = game_menu.addAction("Hint")
        act_hint.triggered.connect(self._hint)  # type: ignore[attr-defined]
        act_solve = game_menu.addAction("Solve")
        act_solve.triggered.connect(self._solve)  # type: ignore[attr-defined]

        view_menu = self.menuBar().addMenu("&View")
        act_theme = view_menu.addAction("Toggle Theme")
        act_theme.triggered.connect(self._toggle_theme)  # type: ignore[attr-defined]

        help_menu = self.menuBar().addMenu("&Help")
        act_about = help_menu.addAction("About")
        act_about.triggered.connect(self._about)  # type: ignore[attr-defined]

    def _refresh(self) -> None:
        self.board_widget.set_board(self.service.board)
        msg = "Complete!" if self.service.is_complete() else ""
        self.status_info.setText(msg)

    def _new_puzzle(self) -> None:
        self.service.new_puzzle(self.level_combo.currentText())
        self._refresh()

    def _hint(self) -> None:
        h = self.service.get_hint()
        if not h:
            QMessageBox.information(self, "Hint", "No logical hint found.")
            return
        expl = str(h.get("explanation", ""))
        QMessageBox.information(self, "Hint", expl)
        self._refresh()

    def _solve(self) -> None:
        if self.service.solve():
            self._refresh()

    def _open(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Open Puzzle", "", "JSON (*.json)")
        if path:
            self.service.import_json(Path(path))
            self._refresh()

    def _save(self) -> None:
        path, _ = QFileDialog.getSaveFileName(self, "Save Puzzle", "", "JSON (*.json)")
        if path:
            self.service.export_json(Path(path))

    def _undo(self) -> None:
        if self.service.undo():
            self._refresh()

    def _redo(self) -> None:
        if self.service.redo():
            self._refresh()

    def _on_cell_edited(self, r: int, c: int, v: int) -> None:
        if not self.service.set_cell(r, c, v):
            self._refresh()
        else:
            self._refresh()

    def _on_level_changed(self, level: str) -> None:
        self.service.level = level

    def _toggle_theme(self) -> None:
        current = self.property("theme") or "light"
        self._apply_theme("dark" if current == "light" else "light")

    def _apply_theme(self, theme: str) -> None:
        self.setProperty("theme", theme)
        self.setStyleSheet(STYLE_DARK if theme == "dark" else STYLE_LIGHT)

    def _about(self) -> None:
        QMessageBox.about(
            self,
            "About SudokuTrainer",
            "SudokuTrainer 0.2.0\nAuthor: Milenkhov\nLicense: MIT\nRepo: https://github.com/Milenkhov/SudokuTrainer",
        )
