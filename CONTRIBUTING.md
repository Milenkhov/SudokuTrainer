# Contributing

Thank you for improving SudokuTrainer!

## Dev setup

- Python 3.11 or 3.12
- Create a venv and install deps:
	- `python -m venv .venv`
	- Windows: `.\.venv\Scripts\activate`
	- `pip install -e ".[dev,gui]"`

## Run locally (GUI)

- Launch the app:
	- `python -m sudokutrainer`
- Features to try: New, Hint, Check, Solve, Undo/Redo.

## Quality checks

- Tests: `pytest -q`
- Lint/format/typecheck: `ruff check . && black --check . && mypy .`

## Packaging (Windows)

- Build a Windows executable:
	- `pyinstaller --clean -y packaging/pyinstaller_win.spec`
	- Output: `dist/SudokuTrainer.exe` (single-file) or a zip as part of release packaging.

## Conventions

- Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `ci:`
- Add/maintain tests where public behavior changes.
- Keep code formatted (ruff+black) and typed (mypy clean).
