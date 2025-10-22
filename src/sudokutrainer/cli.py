from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from .core.board import Board
from .generator.generator import generate
from .hints.engine import next_hint
from .io.formats import load_json_board, save_json_board
from .solver.backtracking import solve
from .solver.rating import rate_board

app = typer.Typer(help="Sudoku Trainer CLI")
console = Console()
_session: dict[str, Board] = {"board": Board.empty()}


def _get_board() -> Board:
    return _session["board"]


@app.command("new")
def new(level: str = typer.Option("Medium", "--level", "-l", help="Difficulty level")) -> None:
    b, rated = generate(level)
    _session["board"] = b
    console.print(f"Generated puzzle rated: [bold]{rated}[/bold]")
    show()


@app.command("show")
def show() -> None:
    b = _get_board()
    table = Table(show_header=False, box=None)
    for r in range(9):
        row = ["." if v == 0 else str(v) for v in b.grid[r]]
        table.add_row(" ".join(row))
    console.print(table)


@app.command("set")
def set_value(row: int, col: int, val: int) -> None:
    b = _get_board()
    b.set_cell(row - 1, col - 1, val)
    console.print(f"Set ({row},{col}) = {val}")
    show()


@app.command("hint")
def hint() -> None:
    b = _get_board()
    h = next_hint(b)
    if not h:
        console.print("No logical hint found.")
        return
    console.print(f"[bold]{h['strategy']}[/bold]: {h['explanation']}")
    move = h.get("suggested_move")
    if isinstance(move, dict):
        r, c, v = move["row"], move["col"], move["value"]
        console.print(f"Try placing {v} at ({r+1},{c+1}).")


@app.command("solve")
def solve_cmd(explain: bool = typer.Option(False, "--explain")) -> None:
    b = _get_board()
    solved, steps = solve(b, explain=explain)
    if not solved:
        console.print("Unsolvable.")
        return
    _session["board"] = solved
    console.print("Solved.")
    if explain:
        for s in steps[:50]:
            console.print(f"- {s}")
        if len(steps) > 50:
            console.print("...")

    show()


@app.command("rate")
def rate() -> None:
    b = _get_board()
    label, counts = rate_board(b)
    console.print(f"Rating: [bold]{label}[/bold] -> {counts}")


@app.command("save")
def save_cmd(path: Path) -> None:
    save_json_board(_get_board(), path)
    console.print(f"Saved to {path}")


@app.command("load")
def load_cmd(path: Path) -> None:
    _session["board"] = load_json_board(path)
    console.print(f"Loaded {path}")
    show()


@app.command("tutorial")
def tutorial() -> None:
    console.print("Tutorial:")
    console.print("- Start with Singles.")
    console.print("- Then look for Pairs and simple eliminations.")
