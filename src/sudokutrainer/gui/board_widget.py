from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

from ..core.board import Board


class BoardWidget(QTableWidget):
    cellEdited = Signal(int, int, int)  # r, c, value

    def __init__(self, parent: QWidget | None = None):
        super().__init__(9, 9, parent)
        self._init_table()

    def _init_table(self) -> None:
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionMode(QTableWidget.SingleSelection)
        self.setSelectionBehavior(QTableWidget.SelectItems)
        for r in range(9):
            self.setRowHeight(r, 36)
        for c in range(9):
            self.setColumnWidth(c, 36)
        for r in range(9):
            for c in range(9):
                it = QTableWidgetItem("")
                it.setTextAlignment(Qt.AlignCenter)
                self.setItem(r, c, it)

    def set_board(self, board: Board) -> None:
        for r in range(9):
            for c in range(9):
                v = board.grid[r][c]
                it = self.item(r, c)
                if it is None:
                    it = QTableWidgetItem("")
                    self.setItem(r, c, it)
                it.setText("" if v == 0 else str(v))
                it.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.viewport().update()

    def keyPressEvent(self, event: QKeyEvent) -> None:  # type: ignore[override]
        idx = self.currentIndex()
        r, c = idx.row(), idx.column()
        if r < 0 or c < 0:
            return super().keyPressEvent(event)
        key = event.key()
        if Qt.Key_1 <= key <= Qt.Key_9:
            val = key - Qt.Key_0
            self.cellEdited.emit(r, c, val)
            return
        if key in (Qt.Key_Backspace, Qt.Key_Delete, Qt.Key_0, Qt.Key_Period):
            self.cellEdited.emit(r, c, 0)
            return
        # navigation
        if key in (Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down):
            dr = -1 if key == Qt.Key_Up else 1 if key == Qt.Key_Down else 0
            dc = -1 if key == Qt.Key_Left else 1 if key == Qt.Key_Right else 0
            nr, nc = max(0, min(8, r + dr)), max(0, min(8, c + dc))
            self.setCurrentCell(nr, nc)
            return
        super().keyPressEvent(event)
