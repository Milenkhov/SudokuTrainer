from sudokutrainer.generator.generator import generate
from sudokutrainer.solver.backtracking import count_solutions


def test_generate_medium_unique() -> None:
    p, rated = generate("Medium")
    assert count_solutions(p, limit=2) == 1
    assert rated in {"Beginner", "Easy", "Medium", "Hard", "Expert"}
