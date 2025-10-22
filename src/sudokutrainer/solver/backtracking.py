from __future__ import annotations

import random

from ..core.board import Board


def solve(board: Board, explain: bool = False) -> tuple[Board | None, list[str]]:
    steps: list[str] = []
    b = board.copy()

    def dfs() -> bool:
        pos = b.first_empty()
        if pos is None:
            return True
        r, c = pos
        cand = list(b.candidates(r, c))
        random.shuffle(cand)
        for v in cand:
            b.grid[r][c] = v
            if explain:
                steps.append(f"Place {v} at ({r+1},{c+1})")
            if dfs():
                return True
            b.grid[r][c] = 0
        return False

    ok = dfs()
    return (b if ok else None, steps)


def count_solutions(board: Board, limit: int = 2) -> int:
    b = board.copy()
    count = 0

    def dfs() -> None:
        nonlocal count
        if count >= limit:
            return
        pos = b.first_empty()
        if pos is None:
            count += 1
            return
        r, c = pos
        for v in sorted(b.candidates(r, c)):
            b.grid[r][c] = v
            dfs()
            if count >= limit:
                return
            b.grid[r][c] = 0

    dfs()
    return count
