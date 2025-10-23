from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..core.board import Board
from ..generator.generator import generate
from ..hints.engine import next_hint
from ..io.formats import load_json_board, save_json_board
from ..solver.backtracking import solve


@dataclass
class GameService:
    level: str = "Medium"
    board: Board = field(default_factory=Board.empty)
    undo_stack: list[str] = field(default_factory=list)
    redo_stack: list[str] = field(default_factory=list)
    notes_mode: bool = False
    givens: set[tuple[int, int]] = field(default_factory=set)
    solution: Board | None = None

    def snapshot(self) -> str:
        return self.board.as_string()

    def restore(self, state: str) -> None:
        self.board = Board.from_string(state)

    def push_undo(self) -> None:
        self.undo_stack.append(self.snapshot())
        self.redo_stack.clear()

    def new_puzzle(self, level: str | None = None) -> None:
        if level:
            self.level = level
        self.push_undo()
        grid, _rated = generate(self.level)
        self.adopt_puzzle(grid)

    def adopt_puzzle(self, grid: Board) -> None:
        """Replace current board with a new puzzle and recompute givens/solution."""
        self.board = grid
        # Record givens from generated puzzle and pre-compute solution for checking
        self.givens = {(r, c) for r in range(9) for c in range(9) if self.board.grid[r][c] != 0}
        self.solution, _ = solve(self.board)

    def set_cell(self, r: int, c: int, v: int) -> bool:
        # Disallow editing of given cells
        if (r, c) in self.givens:
            return False
        prev = self.snapshot()
        # Lenient entry: allow any 0..9 without candidate validation
        if not (0 <= r < 9 and 0 <= c < 9) or v not in range(0, 10):
            return False
        self.board.grid[r][c] = v
        self.undo_stack.append(prev)
        self.redo_stack.clear()
        return True

    def clear_cell(self, r: int, c: int) -> bool:
        return self.set_cell(r, c, 0)

    def get_hint(self) -> dict[str, Any] | None:
        return next_hint(self.board)

    def apply_hint(self) -> bool:
        h = self.get_hint()
        if not h:
            return False
        move = h.get("suggested_move")
        if isinstance(move, dict):
            r, c, v = int(move["row"]), int(move["col"]), int(move["value"])
            return self.set_cell(r, c, v)
        return False

    def solve(self) -> bool:
        solved, _ = solve(self.board)
        if not solved:
            return False
        self.push_undo()
        self.board = solved
        return True

    def is_complete(self) -> bool:
        return self.board.is_complete()

    def export_json(self, path: Path) -> None:
        save_json_board(self.board, path)

    def import_json(self, path: Path) -> None:
        self.push_undo()
        self.board = load_json_board(path)
        self.givens = {(r, c) for r in range(9) for c in range(9) if self.board.grid[r][c] != 0}
        self.solution, _ = solve(self.board)

    def undo(self) -> bool:
        if not self.undo_stack:
            return False
        state = self.undo_stack.pop()
        self.redo_stack.append(self.snapshot())
        self.restore(state)
        return True

    def redo(self) -> bool:
        if not self.redo_stack:
            return False
        state = self.redo_stack.pop()
        self.undo_stack.append(self.snapshot())
        self.restore(state)
        return True

    def has_conflicts(self) -> bool:
        # Check for duplicates in any row/col/box (ignoring zeros)
        def dup(vals: list[int]) -> bool:
            seen: set[int] = set()
            for v in vals:
                if v == 0:
                    continue
                if v in seen:
                    return True
                seen.add(v)
            return False

        b = self.board
        # Rows and columns
        for i in range(9):
            if dup(b.get_row(i)) or dup(b.get_col(i)):
                return True
        # Boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                vals = [b.grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
                if dup(vals):
                    return True
        return False

    def compare_with_solution(self) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        """Return (correct_cells, wrong_cells) comparing non-given entries to solution."""
        correct: set[tuple[int, int]] = set()
        wrong: set[tuple[int, int]] = set()
        if not self.solution:
            return correct, wrong
        for r in range(9):
            for c in range(9):
                if (r, c) in self.givens:
                    continue
                v = self.board.grid[r][c]
                if v == 0:
                    continue
                if self.solution.grid[r][c] == v:
                    correct.add((r, c))
                else:
                    wrong.add((r, c))
        return correct, wrong
