from __future__ import annotations

import random

from ..core.board import Board
from ..solver.backtracking import count_solutions
from ..solver.rating import rate_board
from .presets import PRESETS


def _generate_full() -> Board:
    b = Board.empty()

    def dfs() -> bool:
        pos = b.first_empty()
        if pos is None:
            return True
        r, c = pos
        nums = list(range(1, 10))
        random.shuffle(nums)
        for v in nums:
            if v in b.candidates(r, c):
                b.grid[r][c] = v
                if dfs():
                    return True
                b.grid[r][c] = 0
        return False

    dfs()
    return b


def _dig_to_puzzle(full: Board, min_givens: int) -> Board:
    b = full.copy()
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells:
        if sum(1 for rr in range(9) for cc in range(9) if b.grid[rr][cc] != 0) <= min_givens:
            break
        backup = b.grid[r][c]
        b.grid[r][c] = 0
        if count_solutions(b, limit=2) != 1:
            b.grid[r][c] = backup
    return b


def generate(level: str) -> tuple[Board, str]:
    level = level.capitalize()
    if level not in PRESETS:
        raise ValueError(f"Unknown level: {level}")
    min_clues, max_clues = PRESETS[level]
    # Try until rating matches desired label (cap iterations to keep tests fast)
    for _ in range(12):
        full = _generate_full()
        # choose target clues in preset window
        target_givens = random.randint(min_clues, max_clues)
        puzzle = _dig_to_puzzle(full, min_givens=target_givens)
        rating_label, _ = rate_board(puzzle)
        if rating_label == level and count_solutions(puzzle, limit=2) == 1:
            return puzzle, rating_label
    # Fallback: return last puzzle with computed rating
    return puzzle, rating_label
