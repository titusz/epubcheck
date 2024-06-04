import sys
from subprocess import run


def test_cli_module():
    result = run([sys.executable, "-m", "epubcheck", "-h"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "EpubCheck" in result.stdout
