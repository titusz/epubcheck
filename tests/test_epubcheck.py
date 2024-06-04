import subprocess
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
