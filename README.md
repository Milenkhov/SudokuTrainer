# SudokuTrainer

SudokuTrainer is a desktop Sudoku app for Windows. Generate puzzles, get human-style hints, and check your progress with one click.

Highlights:
- Difficulty levels: Beginner, Easy, Medium, Hard, Expert
- Generator with uniqueness guarantee and difficulty targeting
- Human-style hints: Naked/Hidden Single, Naked Pair, eliminations
- New: Check button to highlight correct/incorrect entries
- New: Thick 3×3 grid lines for better readability (like a classic Sudoku)
- New: View > Show Coordinates toggle (x,y) headers on/off
- New: Non-blocking “New” (async generation) so the UI stays responsive

## Download and run (Windows)

1) Download the latest release from:
	https://github.com/Milenkhov/SudokuTrainer/releases

Direct download links for v0.2.4:
- EXE (single file): https://github.com/Milenkhov/SudokuTrainer/releases/download/v0.2.4/SudokuTrainer.exe
- ZIP (contains EXE + checksum): https://github.com/Milenkhov/SudokuTrainer/releases/download/v0.2.4/SudokuTrainer-0.2.4-Windows-x64.zip

2) Option A: Run the single-file EXE directly.

3) Option B: Extract the ZIP and double‑click `SudokuTrainer.exe`.

- The single-file .exe runs without extracting.
- No Python required for the Windows build.

## Using the app

- New: Choose difficulty and click "New" to generate a puzzle.
- Type digits 1–9 into empty cells. You can make mistakes; the app won't block invalid entries.
- View > Show Coordinates: Toggle row/column headers if you find them distracting.
- Hint: Shows a logical hint when the board has no conflicts.
- Check: Colors entries you added: green if correct, red if incorrect. Use it any time to assess progress.
- Solve: Fills in the solution if you want to see the completed grid.

### Quick rules (How to play)

- Each row must contain digits 1–9 exactly once.
- Each column must contain digits 1–9 exactly once.
- Each 3×3 box must contain digits 1–9 exactly once.

Tips: Start with singles, use Check to assess progress, and ask for a Hint when there are no conflicts.

Note on Python 3.14 for developers: PySide6/PyInstaller availability may lag. The project gates GUI deps on Python < 3.14; use Python 3.11/3.12 for development and packaging.

## Releases

- Releases include a Windows build. Download from:
	https://github.com/Milenkhov/SudokuTrainer/releases
- Preferred assets:
  - Single-file EXE for quick run
  - Or the ZIP: `SudokuTrainer-<tag>-Windows-x64.zip` (extract and run)

## Verify downloads (SHA256)

Verifying your download protects you from corruption or tampering. It’s simple:

- Download the app and the matching “.sha256.txt” file from the same release.
- Open the “.sha256.txt” file and note the long SHA256 value next to the filename.
- Use any checksum tool to compute the SHA256 of your downloaded file.
- The two values must match exactly. If they don’t, re‑download from the release page.

Checksum files for v0.2.4:
- EXE SHA256: https://github.com/Milenkhov/SudokuTrainer/releases/download/v0.2.4/SudokuTrainer.exe.sha256.txt
- ZIP SHA256: https://github.com/Milenkhov/SudokuTrainer/releases/download/v0.2.4/SudokuTrainer-0.2.4-Windows-x64.zip.sha256.txt

## Development

- Requirements: Python 3.11 or 3.12.
- Install: `python -m venv .venv && .\.venv\Scripts\activate && pip install -e ".[dev,gui]"`
- Run the GUI: `python -m sudokutrainer`
- Tests: `pytest -q`
- Lint/format/typecheck: `ruff check . && black --check . && mypy .`

License: MIT
