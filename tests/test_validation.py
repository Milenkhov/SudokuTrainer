from sudokutrainer.core.board import Board
from sudokutrainer.core.validation import is_valid_board


def test_is_valid_board() -> None:
    b = Board.from_string(
        "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    )
    assert is_valid_board(b)
