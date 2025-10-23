# Changelog

All notable changes to this project will be documented here.

## [0.2.3] - 2025-10-23
### Fixed
- Windows executable failed to start due to relative import in `__main__`. Switched to absolute import to work under PyInstaller.

### Changed
- Release workflow now zips and uploads a single Windows artifact per tag for easier downloads.
- Python version in Release workflow set to 3.12 to match local packaging environment.

### Cleanups
- Removed unused GUI placeholder files to reduce clutter.
- Ignored `tmp_cli.json` (CLI session cache) and removed it from tracking.

## [0.2.2] - 2025-10-22
### Fixed
- PyInstaller spec updated to include PySide6 hidden imports and data files (Qt plugins/resources), improving Windows runtime reliability.

## [0.2.1] - 2025-10-22
### Fixed
- Packaging pipeline adjustments: move PySide6 to optional `[gui]` extra; Release job installs `.[dev,gui]` only where needed.

## [0.2.0] - 2025-10-22
### Added
- GUI scaffolding with PySide6: `MainWindow`, `BoardWidget`, theming, menus/toolbars, and basic interactions.
- CLI command `sudoku gui` to launch the GUI.
- Windows packaging via PyInstaller and automated Release workflow on tag push.
- GUI smoke test that runs offscreen in CI.

### Changed
- Project version bumped to 0.2.0.
- Development ergonomics: VS Code configs and type annotations in GUI components.

### Notes
- Local installation on Python 3.14 skips PySide6/PyInstaller (not yet available) via environment markers; CI uses Python 3.11 to build GUI artifacts.

## [0.1.0] - 2025-10-22
### Added
- Initial MVP: generator (unique), solver (backtracking), human strategies (naked/hidden singles, pairs), rating, hints, CLI.
- Tests with coverage target > 80%.
- CI workflow, pre-commit hooks, docs.
