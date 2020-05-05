from file_util import File
from pathlib import Path

CONTENT = "content"


def test_read(tmp_path: Path):

    file_path = str(tmp_path.joinpath("file.txt"))
    File(file_path).write(CONTENT)
    assert File(file_path).read() == CONTENT


def test_does_not_exists(tmp_path: Path):
    file_path = str(tmp_path.joinpath("file.txt"))
    _file = File(file_path)
    assert _file.does_not_exists
    _file.create()
    assert _file.exists
