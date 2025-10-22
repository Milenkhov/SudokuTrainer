from sudokutrainer.core.board import Board
from sudokutrainer.hints.engine import next_hint


def test_naked_single_hint_exists_on_simple_board() -> None:
    # Construct a nearly-complete row to force a naked single
    s = (
        "530070000"
        "600195000"
        "098000060"
        "800060003"
        "400803001"
        "700020006"
        "060000280"
        "000419005"
        "000080079"
    )
    b = Board.from_string(s)
    h = next_hint(b)
    assert h is not None
    assert "strategy" in h
