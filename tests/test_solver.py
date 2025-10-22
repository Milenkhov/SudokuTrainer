from sudokutrainer.core.board import Board
from sudokutrainer.solver.backtracking import solve


def test_solver_solves_known_puzzle() -> None:
    b = Board.from_string(
        "000260701680070090190004500820100040004602900050003028009300074040050036703018000"
    )
    solved, _ = solve(b)
    assert solved is not None
    assert solved.is_complete()
