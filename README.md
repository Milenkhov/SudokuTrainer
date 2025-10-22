# SudokuTrainer

Text-based Sudoku trainer with generator, solver, and human-style hints.

Features:
- Difficulty: Beginner, Easy, Medium, Hard, Expert
- Generator: uniqueness guaranteed, difficulty targeted
- Solver: backtracking + human strategies
- Hints: Naked Single, Hidden Single, Naked Pair, Hidden Pair, Eliminations
- CLI: `sudoku` command

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

License: MIT
