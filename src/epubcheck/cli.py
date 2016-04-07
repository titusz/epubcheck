# -*- coding: utf-8 -*-
"""
Module that contains the command line app.
"""
from __future__ import unicode_literals, print_function
import os
import sys
from six.moves import getcwd
from argparse import ArgumentParser, FileType
from multiprocessing.dummy import Pool as ThreadPool
import tablib
from epubcheck import __version__, EpubCheck
from epubcheck.models import Checker, Meta
from epubcheck.utils import iter_files


def create_parser():
    """Creat a commandline parser for epubcheck

    :return Argumentparser:
    """

    parser = ArgumentParser(
        prog='epubcheck',
        description="EpubCheck v%s - Validate your ebooks" % __version__
    )

    # Arguments
    parser.add_argument(
        'infile',
        nargs='?',
        type=FileType(mode='rb'),
        help="Path to EPUB-file to validate"
    )

    # Options
    parser.add_argument(
        '-p', '--path', help="Path to folder with EPUB files for batch validation"
    )
    parser.add_argument(
        '-r', '--recursive', action='store_true', help='Recurse into subfolders'
    )

    return parser


def main(argv=None):
    """Command line app main function.

    :param list | None argv: Overrides command options (for libuse or testing)
    """

    parser = create_parser()
    args = parser.parse_args() if argv is None else parser.parse_args(argv)

    if not args.infile and not args.path:
        args.path = getcwd()

    all_valid = True
    tpl = 'Finished validating {}: {}'

    if args.infile:
        print('Validating %s' % args.infile.name)
        result = EpubCheck(args.infile.name)
        for msg in result.messages:
            print(msg.short, file=sys.stderr)
        if result.valid:
            print(tpl.format(result.checker.filename, 'VALID'))
        else:
            print(tpl.format(result.checker.filename, 'INVALID'))
            all_valid = False

    if args.path:
        tree_or_dir = 'tree' if args.recursive else 'dir'
        print('\nValidating all files in %s %s' % (tree_or_dir, args.path))
        pool = ThreadPool()
        files = iter_files(args.path, ('epub',), args.recursive)
        results = pool.imap_unordered(EpubCheck, files)
        data = tablib.Dataset(headers=Checker._fields + Meta._fields)

        for result in results:
            fname = result.checker.filename
            msg = tpl.format(fname, 'Valid' if result.valid else 'INVALID')
            data.append(result.checker + result.meta.flatten())
            if result.valid:
                print(msg)
            else:
                print(msg, file=sys.stderr)
                all_valid = False

        pool.close()

        print('Writing epubcheck-result.xls')
        outpath = os.path.join(getcwd(), 'epubcheck-result.xls')
        with open(outpath, 'wb') as outf:
            outf.write(data.xls)

    if all_valid:
        return 0
    else:
        return 1
