import subprocess
import pytest
import tablib
import epubcheck
from epubcheck import samples
from epubcheck.cli import main


def test_valid():
    assert epubcheck.validate(samples.EPUB3_VALID)


def test_invalid():
    assert not epubcheck.validate(samples.EPUB3_INVALID)


def test_main_valid(capsys):
    argv = [samples.EPUB3_VALID]
    exit_code = main(argv)
    out, err = capsys.readouterr()
    assert "ERROR" not in out and "ERROR" not in err
    assert exit_code == 0


def test_main_invalid(capsys):
    argv = [samples.EPUB3_INVALID]
    exit_code = main(argv)
    out, err = capsys.readouterr()
    assert "ERROR" in err and "WARNING" in out
    assert exit_code == 1


def test_reports_use_default_filenames(tmp_path, monkeypatch):
    """Bare --xls/--csv fall back to their `const` filenames in the working directory."""
    monkeypatch.chdir(tmp_path)
    main([samples.EPUB3_INVALID, "--xls", "--csv"])

    assert (tmp_path / "epubcheck_report.csv").stat().st_size > 0
    assert (tmp_path / "epubcheck_report.xls").stat().st_size > 0


def test_report_target_stdout(capsysbinary):
    """`-` streams the report to stdout instead of creating a file named `-`."""
    exit_code = main([samples.EPUB3_INVALID, "--csv", "-"])
    out, err = capsysbinary.readouterr()

    assert exit_code == 1
    assert b"OPF-004;WARNING" in out


def test_unwritable_report_target_fails_fast(capsys, tmp_path):
    """An unusable report path aborts with a usage error before any validation runs."""
    target = tmp_path / "missing_dir" / "report.csv"

    with pytest.raises(SystemExit) as excinfo:
        main([samples.EPUB3_INVALID, "--csv", str(target)])
    out, err = capsys.readouterr()

    assert excinfo.value.code == 2
    assert "can't open" in err
    assert "WARNING" not in out


def test_missing_path(capsys, tmp_path):
    """A path that does not exist is reported instead of silently succeeding."""
    exit_code = main([str(tmp_path / "no_such_book.epub")])
    out, err = capsys.readouterr()

    assert exit_code == 1
    assert "no such file or directory" in err


def test_csv_report(tmp_path):
    results_file = tmp_path / "results.csv"
    main([samples.EPUB3_INVALID, "--csv", str(results_file)])

    with results_file.open("r") as f:
        dataset = tablib.Dataset().load(f.read(), format="csv", delimiter=";")
        assert dataset[0][:3] == (
            "OPF-004",
            "WARNING",
            "invalid.epub/EPUB/package.opf:1:129",
        )


def test_xls_report(tmp_path):
    results_file = tmp_path / "results.xls"
    main([samples.EPUB3_INVALID, "--xls", results_file.as_posix()])

    with results_file.open("rb") as f:
        databook = tablib.import_set(f, "xls")
        assert databook.headers == [
            "path",
            "filename",
            "checkerVersion",
            "checkDate",
            "elapsedTime",
            "nFatal",
            "nError",
            "nWarning",
            "nUsage",
            "publisher",
            "title",
            "creator",
            "date",
            "subject",
            "description",
            "rights",
            "identifier",
            "language",
            "nSpines",
            "checkSum",
            "renditionLayout",
            "renditionOrientation",
            "renditionSpread",
            "ePubVersion",
            "isScripted",
            "hasFixedFormat",
            "isBackwardCompatible",
            "hasAudio",
            "hasVideo",
            "charsCount",
            "embeddedFonts",
            "refFonts",
            "hasEncryption",
            "hasSignatures",
            "contributors",
        ]
