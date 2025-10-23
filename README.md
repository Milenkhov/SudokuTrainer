# SudokuTrainer

Text-based Sudoku trainer with generator, solver, and human-style hints. Now with a GUI.

Features:
- Difficulty: Beginner, Easy, Medium, Hard, Expert
- Generator: uniqueness guaranteed, difficulty targeted
- Solver: backtracking + human strategies
- Hints: Naked Single, Hidden Single, Naked Pair, Hidden Pair, Eliminations
- CLI: `sudoku` command
- GUI: `sudoku gui` or run the packaged Windows build from Releases

Quick start (uv):

```
uv venv
uv sync
uv run sudoku new --level Medium
uv run sudoku show
uv run sudoku hint
uv run sudoku solve --explain
```

Quick start (pip):

```
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"
sudoku new --level Medium
sudoku show
sudoku hint
sudoku solve --explain
```

Troubleshooting:
- Ensure Python 3.11+.
- Run tests: `pytest -q`
- Lint: `ruff check .` and `black --check .` and `mypy .`

## GUI

- Run from CLI: `sudoku gui`
- Or run as a module: `python -m sudokutrainer` (launches the GUI)
- Windows builds are attached to GitHub Releases when tags are pushed (CI builds on Python 3.11).

Note on Python 3.14: PySide6 and PyInstaller may not be available yet. The project gates these dependencies on Python < 3.14 so installs succeed; use Python 3.11/3.12 locally for GUI development and packaging.

## VS Code

- Use the provided launch configurations (CLI helpers). You can add a GUI launcher by running the CLI with args `gui`.

License: MIT
