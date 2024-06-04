# -*- coding: utf-8 -*-
"""
Module that contains the command line app.
"""

from __future__ import unicode_literals, print_function
import os
import sys
from argparse import ArgumentParser, FileType
from multiprocessing.dummy import Pool as ThreadPool
import tablib
from epubcheck import __version__, EpubCheck
from epubcheck.models import Checker, Meta, Message
from epubcheck.utils import iter_files
from epubcheck import compat

if compat.PY2:
    from os import getcwdu as getcwd  # pragma: no cover
else:
    from os import getcwd


def create_parser():
    """Creat a commandline parser for epubcheck

    :return Argumentparser:
    """

    parser = ArgumentParser(
        prog="epubcheck",
        description="EpubCheck v%s - Validate your ebooks" % __version__,
    )

    # Arguments
    parser.add_argument(
        "path",
        nargs="?",
        default=getcwd(),
        help="Path to EPUB-file or folder for batch validation. "
        "The current directory will be processed if this argument "
        "is not specified.",
    )

    # Options
    parser.add_argument(
        "-x",
        "--xls",
        nargs="?",
        type=FileType(mode="wb"),
        const="epubcheck_report.xls",
        help="Create a detailed Excel report.",
    )

    parser.add_argument(
        "-c",
        "--csv",
        nargs="?",
        type=FileType(mode="wb"),
        const="epubcheck_report.csv",
        help="Create a CSV report.",
    )

    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subfolders.")

    return parser


def main(argv=None):
    """Command line app main function.

    :param list | None argv: Overrides command options (for libuse or testing)
    """

    parser = create_parser()
    args = parser.parse_args() if argv is None else parser.parse_args(argv)

    if not os.path.exists(args.path):
        sys.exit(0)  # pragma: no cover

    all_valid = True
    single = os.path.isfile(args.path)
    files = (
        [args.path] if single else iter_files(args.path, exts=("epub",), recursive=args.recursive)
    )

    pool = ThreadPool()
    results = pool.imap_unordered(EpubCheck, files)

    metas = tablib.Dataset(headers=Checker._fields + Meta._fields)
    messages = tablib.Dataset(headers=Message._fields)

    for result in results:
        metas.append(result.checker + result.meta.flatten())
        if not result.valid:
            all_valid = False
        for message in result.messages:
            messages.append(message)
            if message.level == "ERROR":
                print(message.short, file=sys.stderr)
            else:
                print(message.short)

    if args.csv:
        args.csv.write(messages.export("csv", delimiter=compat.text_type(";")).encode())
        args.csv.close()

    if args.xls:
        databook = tablib.Databook((metas, messages))
        args.xls.write(bytes(databook.export("xls")))
        args.xls.close()

    if all_valid:
        return 0
    else:
        return 1
