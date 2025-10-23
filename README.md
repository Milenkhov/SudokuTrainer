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

2) Extract `SudokuTrainer-<tag>-win64.zip` and double‑click `SudokuTrainer.exe`.

- Single-file .exe may also be provided; if available, you can run it directly without extracting.
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
- Preferred asset: `SudokuTrainer-<tag>-win64.zip` (extract and run). A single-file `.exe` may also be attached when available.

## Verify downloads (SHA256)

To verify your download's integrity, compare its SHA256 hash against the official checksum file attached to the release.

- Checksum file for v0.2.3:
	https://github.com/Milenkhov/SudokuTrainer/releases/download/v0.2.3/SudokuTrainer-v0.2.3-win64.sha256.txt
- For newer versions, open the corresponding release and download the matching `.sha256.txt` file.

Windows PowerShell example:

```
# From the folder where you downloaded the files
Get-FileHash -Algorithm SHA256 .\SudokuTrainer.exe
Get-FileHash -Algorithm SHA256 .\SudokuTrainer-v0.2.3-win64.zip
Get-FileHash -Algorithm SHA256 .\SudokuTrainer-v0.2.3-win64.tar.gz

# Compare each output Hash to the line for the same filename in the .sha256.txt file
# (Two spaces separate the hash and filename in the checksum file.)
```

Optional: quick boolean checks for all three files at once

```
$checks = Get-Content .\SudokuTrainer-v0.2.3-win64.sha256.txt
$files  = 'SudokuTrainer.exe','SudokuTrainer-v0.2.3-win64.zip','SudokuTrainer-v0.2.3-win64.tar.gz'
$files | ForEach-Object {
	$expected = ($checks | Where-Object { $_ -match ("  " + [regex]::Escape($_) + '$') }) -replace '\s\s.*$',''
	$actual   = (Get-FileHash -Algorithm SHA256 $_).Hash
	'{0}: {1}' -f $_, ($actual -eq $expected)
}
```

## Development

- Requirements: Python 3.11 or 3.12.
- Install: `python -m venv .venv && .\.venv\Scripts\activate && pip install -e ".[dev,gui]"`
- Run the GUI: `python -m sudokutrainer`
- Tests: `pytest -q`
- Lint/format/typecheck: `ruff check . && black --check . && mypy .`

License: MIT
