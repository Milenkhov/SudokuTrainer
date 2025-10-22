from __future__ import annotations

from .board import Board


def _valid_group(values: list[int]) -> bool:
    nums = [v for v in values if v != 0]
    return len(nums) == len(set(nums)) and all(1 <= v <= 9 for v in nums)


def is_valid_board(b: Board) -> bool:
    for i in range(9):
        if not _valid_group(b.get_row(i)):
            return False
        if not _valid_group(b.get_col(i)):
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if not _valid_group(
                [b.grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
            ):
                return False
    return True
