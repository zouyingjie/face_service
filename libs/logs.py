# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals, print_function
import logging


def log_message(message, **kwargs):
    return '[%s]' % message


class InfoFilter(logging.Filter):
    def filter(self, record):
        return 1 if record.levelname in ['DEBUG', 'INFO'] else 0


class WarningFilter(logging.Filter):
    def filter(self, record):
        return 1 if record.levelname in ['WARNING', 'ERROR'] else 0
