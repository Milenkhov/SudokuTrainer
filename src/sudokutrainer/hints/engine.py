from __future__ import annotations

from ..core.board import Board
from ..solver.human_strategies import find_hint


def next_hint(b: Board) -> dict[str, object] | None:
    return find_hint(b)
