from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QKeyEvent, QPainter, QPen
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

from ..core.board import Board


class BoardWidget(QTableWidget):
    cellEdited = Signal(int, int, int)  # r, c, value

    def __init__(self, parent: QWidget | None = None):
        super().__init__(9, 9, parent)
        self._init_table()
        self._given_mask: set[tuple[int, int]] = set()
        self._show_coords: bool = True
        self.setShowGrid(False)  # draw our own grid with thick 3x3 lines

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

    def set_board(self, board: Board, givens: set[tuple[int, int]] | None = None) -> None:
        if givens is not None:
            self._given_mask = set(givens)
        for r in range(9):
            for c in range(9):
                v = board.grid[r][c]
                it = self.item(r, c)
                if it is None:
                    it = QTableWidgetItem("")
                    self.setItem(r, c, it)
                it.setText("" if v == 0 else str(v))
                it.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                # Style givens vs. user entries (theme-aware)
                self._style_cell(r, c, is_given=(r, c) in self._given_mask)
        self.viewport().update()

    def _is_dark(self) -> bool:
        return (self.window().property("theme") or "light") == "dark"

    def _style_cell(self, r: int, c: int, *, is_given: bool) -> None:
        it = self.item(r, c)
        if not it:
            return
        if self._is_dark():
            txt = QColor("#e0e0e0")
            bg_given = QColor("#3a3f44")
            bg_user = QColor("#2b2b2b")
        else:
            txt = QColor("#000000")
            bg_given = QColor("#e9ecef")
            bg_user = QColor("#ffffff")
        it.setForeground(txt)
        it.setBackground(bg_given if is_given else bg_user)
        font = it.font()
        font.setBold(is_given)
        it.setFont(font)

    def set_show_coords(self, show: bool) -> None:
        self._show_coords = show
        self.horizontalHeader().setVisible(show)
        self.verticalHeader().setVisible(show)
        self.viewport().update()

    def clear_highlights(self) -> None:
        # Reset non-given cell backgrounds to default
        for r in range(9):
            for c in range(9):
                it = self.item(r, c)
                if not it:
                    continue
                self._style_cell(r, c, is_given=(r, c) in self._given_mask)
        self.viewport().update()

    def highlight_results(self, correct: set[tuple[int, int]], wrong: set[tuple[int, int]]) -> None:
        for r, c in correct:
            it = self.item(r, c)
            if it:
                it.setBackground(QColor("#d1f7c4"))  # light green
        for r, c in wrong:
            it = self.item(r, c)
            if it:
                it.setBackground(QColor("#f8d7da"))  # light red
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

    def paintEvent(self, event) -> None:  # type: ignore[override]
        super().paintEvent(event)
        # Draw grid with thicker lines at 3x3 boundaries
        painter = QPainter(self.viewport())
        color = QColor("#101010") if not self._is_dark() else QColor("#cfd3d7")
        thin = QPen(color, 1)
        thick = QPen(color, 3)

        # Compute boundaries
        xs = [0]
        x = 0
        for c in range(self.columnCount()):
            x += self.columnWidth(c)
            xs.append(x)
        ys = [0]
        y = 0
        for r in range(self.rowCount()):
            y += self.rowHeight(r)
            ys.append(y)

        for i, xx in enumerate(xs):
            painter.setPen(thick if i % 3 == 0 or i == 9 else thin)
            painter.drawLine(xx, 0, xx, ys[-1])
        for j, yy in enumerate(ys):
            painter.setPen(thick if j % 3 == 0 or j == 9 else thin)
            painter.drawLine(0, yy, xs[-1], yy)
        painter.end()
