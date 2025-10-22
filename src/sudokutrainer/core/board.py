from __future__ import annotations

from dataclasses import dataclass

N = 9
Digits = set[int]
Coord = tuple[int, int]  # (row, col)


@dataclass
class Board:
    grid: list[list[int]]

    @staticmethod
    def empty() -> Board:
        return Board([[0 for _ in range(N)] for _ in range(N)])

    @staticmethod
    def from_list(values: list[list[int]]) -> Board:
        if len(values) != N or any(len(r) != N for r in values):
            raise ValueError("Grid must be 9x9")
        if any(v < 0 or v > 9 for r in values for v in r):
            raise ValueError("Values must be in 0..9")
        return Board([r[:] for r in values])

    @staticmethod
    def from_string(s: str) -> Board:
        s = s.strip().replace(".", "0")
        if len(s) != 81 or any(c not in "0123456789" for c in s):
            raise ValueError("String must be 81 chars of 0-9/.")
        vals = [int(c) for c in s]
        grid = [vals[i * 9 : (i + 1) * 9] for i in range(9)]
        return Board.from_list(grid)

    def copy(self) -> Board:
        return Board.from_list(self.grid)

    def is_complete(self) -> bool:
        return all(all(v != 0 for v in row) for row in self.grid)

    def get_row(self, r: int) -> list[int]:
        return self.grid[r][:]

    def get_col(self, c: int) -> list[int]:
        return [self.grid[r][c] for r in range(N)]

    def get_box(self, r: int, c: int) -> list[int]:
        br, bc = (r // 3) * 3, (c // 3) * 3
        return [self.grid[rr][cc] for rr in range(br, br + 3) for cc in range(bc, bc + 3)]

    def candidates(self, r: int, c: int) -> Digits:
        if self.grid[r][c] != 0:
            return set()
        used = set(self.get_row(r)) | set(self.get_col(c)) | set(self.get_box(r, c))
        return set(range(1, 10)) - used

    def set_cell(self, r: int, c: int, v: int) -> None:
        if not (0 <= r < 9 and 0 <= c < 9):
            raise ValueError("Out of bounds")
        if v not in range(0, 10):
            raise ValueError("Value must be 0..9")
        if v != 0 and v not in self.candidates(r, c):
            raise ValueError("Invalid move")
        self.grid[r][c] = v

    def first_empty(self) -> Coord | None:
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return (r, c)
        return None

    def as_string(self) -> str:
        return "".join(str(v) for row in self.grid for v in row)

    def render(self) -> str:
        def fmt(v: int) -> str:
            return "." if v == 0 else str(v)

        lines = []
        for r in range(9):
            row = " ".join(fmt(v) for v in self.grid[r])
            lines.append(row)
        return "\n".join(lines)
