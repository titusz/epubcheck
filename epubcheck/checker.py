# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
import subprocess
from epubcheck import const as c
from epubcheck.models import Message, Checker, Meta


class EpubCheck:
    """Wraps an epubcheck task and provides results as native python objects.

    :param str infile: path to epubfile to be checked
    :param str lang: set language for generated messages
    :param str profile: name of epubcheck profule to use
    :param bool autorun: wether to run the checking process on instantiation.
    """

    DEFAULT = "default"
    DICT = "dict"
    EDUPUB = "edupub"
    IDX = "idx"
    PREVIEW = "preview"

    def __init__(self, infile, lang="en", profile=DEFAULT, autorun=True):
        self.infile = infile
        self.lang = lang
        self.profile = profile
        self.autorun = autorun

        self._stdout = None
        self._stderr = None
        self._returncode = None
        self._messages = None
        self.result_data = None
        self.valid = None
        self.checker = None
        self.meta = None
        self.messages = None
        if autorun:
            self.run()

    def run(self):
        lopt = "-Duser.language={}".format(self.lang)
        cmd = [
            c.JAVA,
            lopt,
            "-jar",
            c.EPUBCHECK,
            self.infile,
            "-q",
            "--profile",
            self.profile,
            "--json",
            "-",
        ]

        with open(os.devnull, "w") as devnull:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=devnull,
            )

            self._stdout, self._stderr = process.communicate()
            self._returncode = process.returncode
        self.valid = True if self._returncode == 0 else False
        self.result_data = json.loads(self._stdout.decode())
        self.checker = Checker.from_data(self.result_data)
        self.meta = Meta.from_data(self.result_data)
        self.messages = Message.from_data(self.result_data)
