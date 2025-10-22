from pathlib import Path

from sudokutrainer.core.board import Board
from sudokutrainer.io.formats import load_json_board, save_json_board


def test_save_and_load_json(tmp_path: Path) -> None:
    b = Board.from_string(
        "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    )
    p = tmp_path / "puzzle.json"
    save_json_board(b, p)
    b2 = load_json_board(p)
    assert b.as_string() == b2.as_string()
