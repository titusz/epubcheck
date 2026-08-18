"""
Module that contains the command line app.
"""

import os
import sys
from argparse import ArgumentParser
from multiprocessing.dummy import Pool as ThreadPool
import tablib
from epubcheck import __version__, EpubCheck
from epubcheck.models import Checker, Meta, Message
from epubcheck.utils import iter_files


def create_parser():
    """Create a commandline parser for epubcheck

    :return Argumentparser:
    """

    parser = ArgumentParser(
        prog="epubcheck",
        description=f"EpubCheck v{__version__} - Validate your ebooks",
    )

    # Arguments
    parser.add_argument(
        "path",
        nargs="?",
        default=os.getcwd(),
        help="Path to EPUB-file or folder for batch validation. "
        "The current directory will be processed if this argument "
        "is not specified.",
    )

    # Options
    parser.add_argument(
        "-x",
        "--xls",
        nargs="?",
        const="epubcheck_report.xls",
        help="Create a detailed Excel report.",
    )

    parser.add_argument(
        "-c",
        "--csv",
        nargs="?",
        const="epubcheck_report.csv",
        help="Create a CSV report.",
    )

    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subfolders.")

    return parser


def open_report(parser, target):
    """Open a report target for binary writing.

    Maps ``-`` to stdout and turns unusable paths into an argparse usage error,
    mirroring the deprecated ``argparse.FileType`` this replaces. Targets are
    opened before validation starts so bad paths fail fast.

    :param ArgumentParser parser: Parser used to report unusable targets
    :param str | None target: Filesystem path, ``-`` for stdout, or None
    :return tuple | None: ``(file, close_it)`` pair, or None if no target was given
    """

    if target is None:
        return None
    if target == "-":
        return sys.stdout.buffer, False
    try:
        return open(target, "wb"), True
    except OSError as exc:
        parser.error(f"can't open '{target}': {exc}")


def write_report(report, data):
    """Write an encoded report and close the file if we own it.

    :param tuple report: ``(file, close_it)`` pair from :func:`open_report`
    :param bytes data: Encoded report content
    """

    fileobj, close_it = report
    try:
        fileobj.write(data)
        fileobj.flush()
    finally:
        if close_it:
            fileobj.close()


def main(argv=None):
    """Command line app main function.

    :param list | None argv: Overrides command options (for libuse or testing)
    """

    parser = create_parser()
    args = parser.parse_args() if argv is None else parser.parse_args(argv)

    if not os.path.exists(args.path):
        print(f"epubcheck: error: no such file or directory: {args.path}", file=sys.stderr)
        return 1

    csv_report = open_report(parser, args.csv)
    xls_report = open_report(parser, args.xls)

    all_valid = True
    single = os.path.isfile(args.path)
    files = (
        [args.path] if single else iter_files(args.path, exts=("epub",), recursive=args.recursive)
    )

    metas = tablib.Dataset(headers=Checker._fields + Meta._fields)
    messages = tablib.Dataset(headers=Message._fields)

    with ThreadPool() as pool:
        for result in pool.imap_unordered(EpubCheck, files):
            metas.append(result.checker + result.meta.flatten())
            if not result.valid:
                all_valid = False
            for message in result.messages:
                messages.append(message)
                if message.level == "ERROR":
                    print(message.short, file=sys.stderr)
                else:
                    print(message.short)

    if csv_report is not None:
        write_report(csv_report, messages.export("csv", delimiter=";").encode())

    if xls_report is not None:
        databook = tablib.Databook((metas, messages))
        write_report(xls_report, bytes(databook.export("xls")))

    if all_valid:
        return 0
    else:
        return 1
