from typer.testing import CliRunner

from sudokutrainer.cli import app

runner = CliRunner()


def test_cli_new_show_solve() -> None:
    r = runner.invoke(app, ["new", "--level", "Medium"])
    assert r.exit_code == 0
    r = runner.invoke(app, ["show"])
    assert r.exit_code == 0
    r = runner.invoke(app, ["hint"])  # may or may not find a hint
    assert r.exit_code == 0
    r = runner.invoke(app, ["rate"])  # should always print rating
    assert r.exit_code == 0
    # save and load roundtrip
    r = runner.invoke(app, ["save", "tmp_cli.json"])
    assert r.exit_code == 0
    r = runner.invoke(app, ["load", "tmp_cli.json"])
    assert r.exit_code == 0
    r = runner.invoke(app, ["solve"])
    assert r.exit_code == 0
