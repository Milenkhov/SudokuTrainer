# Contributing

Dev setup:
- Python 3.11+
- uv (preferred): `uv venv && uv sync`
- pip alternative: `python -m venv .venv && .\.venv\Scripts\activate && pip install -e ".[dev]"`

Commands:
- Lint: `ruff check . && black . && mypy .`
- Test: `pytest -q`
- Run: `sudoku new --level Medium && sudoku show`

Conventional Commits:
- `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `ci:`

PR guidelines:
- Add/maintain tests (cov > 80%).
- Keep code formatted (ruff+black) and typed (mypy clean).