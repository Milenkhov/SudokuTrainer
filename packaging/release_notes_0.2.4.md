# SudokuTrainer 0.2.4

Date: 2025-10-23

## Highlights
- Classic Sudoku visuals: thicker 3×3 separators and a strong outer border.
- View > Show Coordinates toggle for (x,y) headers.
- Non-blocking “New” puzzle generation (async) with status and busy cursor.
- Dark-mode readability improved; light theme polished.
- Check button: highlights correct (green) and incorrect (red) entries.
- Hints blocked when conflicts are present (safer guidance).
- Help > How to Play in-app rules dialog.

## Changes and fixes
- Asynchronous generation to keep the UI responsive.
- Better contrast for text, headers, and buttons in dark mode; consistency in light mode.
- Minor layout and style tweaks across themes.
- Cleanups: removed unused GUI placeholders; ignored tmp_cli.json; repo hygiene.

## Packaging
- Windows one-file EXE built with PyInstaller.
- Download the ZIP below for convenience.

## Downloads
- SudokuTrainer-0.2.4-Windows-x64.zip
- Checksums:
  - EXE SHA256: BBAB775122E4088E2AC25E1F8EDB29FE0B7415949A453A98E4048336D10774B8
  - ZIP SHA256: see accompanying .zip.sha256.txt in the release assets

## Notes
- Refer to CHANGELOG.md for the full entry.
- If Windows blocks the EXE, use “More info” > “Run anyway”; or unzip and run locally.
