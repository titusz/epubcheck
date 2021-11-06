# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple


_BaseChecker = namedtuple(
    'Checker', 'path filename checkerVersion checkDate elapsedTime nFatal '
               'nError nWarning nUsage')


class Checker(_BaseChecker):
    """Checker related information from epubcheck json data.

    :param str path: Relative path to checked epub
    :param str filename: Filename of checked epub
    :param str checkerVersion: Version string of epubcheck
    :param str checkDate: When the epub was checked
    :param int elapsedTime: processing time
    :param int nFatal: number of fatal errors
    :param int nError: number of errors
    :param int nWarning: number of warnings
    :param int nUsage: number of usage messages
    """

    @classmethod
    def from_data(cls, data):
        return cls(**data['checker'])


_BaseMeta = namedtuple(
    'Meta',
    'publisher title creator date subject description rights identifier '
    'language nSpines checkSum renditionLayout renditionOrientation '
    'renditionSpread ePubVersion isScripted hasFixedFormat isBackwardCompatible '
    'hasAudio hasVideo charsCount embeddedFonts refFonts hasEncryption '
    'hasSignatures contributors '
)


class Meta(_BaseMeta):
    """EPUB metadata from `publication` key in epubcheck json data.

    :param str publisher: name of publisher
    :param str title: title of ebook
    :param list[str] creator: list of creators
    :param str date: date of ebook
    :param list[str] subject: list of ebook subjects
    :param str description: description of ebook
    :param str rights:
    :param str identifier:
    :param str language: language of ebook
    :param int nSpines:
    :param int checkSum:
    :param str renditionLayout:
    :param str renditionSpread:
    :param str ePubVersion:
    :param bool isScripted:
    :param bool hasFixedFormat:
    :param bool isBackwardCompatible:
    :param bool hasAudio:
    :param int charsCount:
    :param list[str] embeddedFonts:
    :param list[str] refFonts:
    :param bool hasEncryption:
    :param bool hasSignatures:
    :param list[str] contributors:
    """

    @classmethod
    def from_data(cls, data):
        return cls(**data['publication'])

    def flatten(self):
        return tuple(';'.join(x) if isinstance(x, list) else x for x in self)


_BaseMessage = namedtuple('Message', 'id level location message suggestion')


class Message(_BaseMessage):
    """
    A Validation message representing a single error condition.

    :param str id: Error type id (ex: "OPF-049")
    :param str level: Severity of messeage (ex: "ERROR")
    :param str location: Location of error (ex: <file>:<line>:<column>)
    :param str message: Description of the error condiction
    :param str suggestion: How to resolve error condition
    """

    def __str__(self):
        return ' | '.join(self._asdict().values())

    @classmethod
    def from_data(cls, data):
        """Create a list of Messages from deserialized epubcheck json output.

        :param dict data: Decoded epubcheck json data
        :return list[Message]: List of messages
        """
        messages = []
        filename = data['checker']['filename']
        for m in data['messages']:
            for l_item in m['locations']:
                location = l_item['path']
                if not location.startswith(filename):
                    location = filename + '/' + location
                if l_item['line'] != -1:
                    location += ':{}'.format(l_item['line'])
                if l_item['column'] != -1:
                    location += ':{}'.format(l_item['column'])
                messages.append(
                    cls(m['ID'], m['severity'], location, m['message'], m['suggestion'])
                )
        return messages

    @property
    def short(self):
        """Short string representation of message"""
        return "{m.level} - {m.id} - {m.location} - {m.message}".format(m=self)
