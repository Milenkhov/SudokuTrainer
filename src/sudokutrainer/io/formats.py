from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core.board import Board


def load_json_board(path: str | Path) -> Board:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and "puzzle" in data:
        return Board.from_string(str(data["puzzle"]))
    raise ValueError("Invalid JSON format. Expected {'puzzle': '...81 chars...'}")


def save_json_board(board: Board, path: str | Path) -> None:
    obj: dict[str, Any] = {"puzzle": board.as_string()}
    Path(path).write_text(json.dumps(obj, indent=2), encoding="utf-8")
