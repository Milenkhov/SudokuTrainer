from __future__ import annotations

from collections import Counter

from ..core.board import Board

Hint = dict[str, object]
Coord = tuple[int, int]


def _naked_single(b: Board) -> Hint | None:
    for r in range(9):
        for c in range(9):
            if b.grid[r][c] == 0:
                cand = b.candidates(r, c)
                if len(cand) == 1:
                    v = next(iter(cand))
                    return {
                        "strategy": "Naked Single",
                        "explanation": f"Only {v} fits at ({r+1},{c+1}).",
                        "affected_cells": [(r, c)],
                        "suggested_move": {"row": r, "col": c, "value": v},
                    }
    return None


def _hidden_single(b: Board) -> Hint | None:
    # rows
    for r in range(9):
        empties = [(r, c) for c in range(9) if b.grid[r][c] == 0]
        counts = Counter(v for (_, c) in empties for v in b.candidates(r, c))
        for v, cnt in counts.items():
            if cnt == 1:
                for _, c in empties:
                    if v in b.candidates(r, c):
                        return {
                            "strategy": "Hidden Single (Row)",
                            "explanation": f"Only position in row {r+1} for {v}.",
                            "affected_cells": [(r, c)],
                            "suggested_move": {"row": r, "col": c, "value": v},
                        }
    # cols
    for c in range(9):
        empties = [(r, c) for r in range(9) if b.grid[r][c] == 0]
        counts = Counter(v for (r, _) in empties for v in b.candidates(r, c))
        for v, cnt in counts.items():
            if cnt == 1:
                for r, _ in empties:
                    if v in b.candidates(r, c):
                        return {
                            "strategy": "Hidden Single (Col)",
                            "explanation": f"Only position in column {c+1} for {v}.",
                            "affected_cells": [(r, c)],
                            "suggested_move": {"row": r, "col": c, "value": v},
                        }
    # boxes
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            cells = [
                (r, c) for r in range(br, br + 3) for c in range(bc, bc + 3) if b.grid[r][c] == 0
            ]
            counts = Counter(v for (r, c) in cells for v in b.candidates(r, c))
            for v, cnt in counts.items():
                if cnt == 1:
                    for r, c in cells:
                        if v in b.candidates(r, c):
                            return {
                                "strategy": "Hidden Single (Box)",
                                "explanation": f"Only position in box ({br//3+1},{bc//3+1}) for {v}.",
                                "affected_cells": [(r, c)],
                                "suggested_move": {"row": r, "col": c, "value": v},
                            }
    return None


def _naked_pair(b: Board) -> Hint | None:
    # rows
    for r in range(9):
        pairs = [(c, b.candidates(r, c)) for c in range(9) if b.grid[r][c] == 0]
        pairs = [(c, cand) for c, cand in pairs if len(cand) == 2]
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                c1, s1 = pairs[i]
                c2, s2 = pairs[j]
                if s1 == s2:
                    eliminated = []
                    for c in range(9):
                        if c not in (c1, c2) and b.grid[r][c] == 0:
                            if len(b.candidates(r, c) & s1):
                                eliminated.append((r, c))
                    if eliminated:
                        v1, v2 = sorted(s1)
                        return {
                            "strategy": "Naked Pair (Row)",
                            "explanation": f"Pair {{{v1},{v2}}} in row {r+1} eliminates from others.",
                            "affected_cells": eliminated,
                            "suggested_move": None,
                        }
    # columns
    for c in range(9):
        pairs = [(r, b.candidates(r, c)) for r in range(9) if b.grid[r][c] == 0]
        pairs = [(r, cand) for r, cand in pairs if len(cand) == 2]
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                r1, s1 = pairs[i]
                r2, s2 = pairs[j]
                if s1 == s2:
                    eliminated = []
                    for r in range(9):
                        if r not in (r1, r2) and b.grid[r][c] == 0:
                            if len(b.candidates(r, c) & s1):
                                eliminated.append((r, c))
                    if eliminated:
                        v1, v2 = sorted(s1)
                        return {
                            "strategy": "Naked Pair (Col)",
                            "explanation": f"Pair {{{v1},{v2}}} in col {c+1} eliminates from others.",
                            "affected_cells": eliminated,
                            "suggested_move": None,
                        }
    return None


def find_hint(b: Board) -> Hint | None:
    # Ordered detection
    return _naked_single(b) or _hidden_single(b) or _naked_pair(b)
