from sudokutrainer.core.board import Board


def test_board_set_and_candidates() -> None:
    b = Board.empty()
    b.set_cell(0, 0, 5)
    assert b.grid[0][0] == 5
    # 5 cannot appear again in row 0
    assert 5 not in b.candidates(0, 1)
