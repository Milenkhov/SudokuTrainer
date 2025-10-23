from __future__ import annotations

STYLE_LIGHT = """
QMainWindow { background: #ffffff; color: #000000; }
QToolBar { background: #f2f2f2; border: 1px solid #d0d0d0; }
QMenuBar, QMenu, QStatusBar { background: #ffffff; color: #000000; }
QPushButton { background: #f0f0f0; border: 1px solid #c8c8c8; padding: 4px 10px; }
QPushButton:hover { background: #e6e6e6; }
QHeaderView::section { background: #f6f6f6; color: #000000; border: 1px solid #cfcfcf; padding: 2px; }
QTableWidget { background: #ffffff; color: #000000; gridline-color: #c0c0c0; }
QTableWidget::item { font-size: 16px; }
QTableWidget::item:selected { background: #cfe8ff; color: #000000; }
"""

STYLE_DARK = """
QMainWindow { background: #1e1e1e; color: #e8e8e8; }
QToolBar { background: #2b2b2b; border: 1px solid #3a3a3a; }
QMenuBar, QMenu, QStatusBar { background: #2b2b2b; color: #e8e8e8; }
QPushButton { background: #3a3f44; color: #e8e8e8; border: 1px solid #555a60; padding: 4px 10px; }
QPushButton:hover { background: #4a5056; }
QHeaderView::section { background: #2e2e2e; color: #e8e8e8; border: 1px solid #555a60; padding: 2px; }
QTableWidget { background: #2b2b2b; color: #e8e8e8; gridline-color: #3a3a3a; }
QTableWidget::item { font-size: 16px; }
QTableWidget::item:selected { background: #25527a; color: #ffffff; }
"""
