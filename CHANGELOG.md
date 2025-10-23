# Changelog

All notable changes to this project will be documented here.

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
