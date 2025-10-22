from __future__ import annotations

from ..core.board import Board
from .human_strategies import find_hint


def rate_board(b: Board) -> tuple[str, dict[str, int]]:
    # Simulate human strategies until stuck; count usage
    tmp = b.copy()
    counts: dict[str, int] = {}
    progress = True
    while progress and not tmp.is_complete():
        progress = False
        hint = find_hint(tmp)
        if not hint:
            break
        strat = str(hint["strategy"])
        counts[strat] = counts.get(strat, 0) + 1
        move = hint.get("suggested_move")
        if isinstance(move, dict):
            r, c, v = move["row"], move["col"], move["value"]
            tmp.grid[r][c] = v
            progress = True
    # Score: singles are easy, pairs harder, anything unresolved bumps difficulty
    score = (
        counts.get("Naked Single", 0) * 1
        + (
            counts.get("Hidden Single (Row)", 0)
            + counts.get("Hidden Single (Col)", 0)
            + counts.get("Hidden Single (Box)", 0)
        )
        * 2
        + (counts.get("Naked Pair (Row)", 0) + counts.get("Naked Pair (Col)", 0)) * 3
    )
    if not tmp.is_complete():
        score += 8  # needs deeper logic/backtracking

    # Map score to label
    if score <= 5:
        label = "Beginner"
    elif score <= 12:
        label = "Easy"
    elif score <= 22:
        label = "Medium"
    elif score <= 35:
        label = "Hard"
    else:
        label = "Expert"
    return label, counts
