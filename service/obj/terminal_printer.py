#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import sys
from typing import ClassVar

from service.obj.abstract_classes import Notifier
from service.obj.constants import DECODING


class StandardResultTerminalPrinter(Notifier):
    """ Класс вывода полей объекта в консоль"""
    DECODING: ClassVar[dict] = DECODING

    def __init__(self, decoding: dict):
        self.DECODING = decoding

    def log(self, obj, message=None, _path=None, _full=False):
        if message:
            sys.stdout.write("\n" + message + "\n")
        for key, val in obj.parameters.items():
            sys.stdout.write(f"{self.DECODING[key].format(obj=val)}\n") if key in self.DECODING else None


class StandardObjectTerminalPrinter(Notifier):
    """ Класс вывода объекта в консоль"""
    def log(self, obj, _message=None, _path=None, _full=False):
        sys.stdout.write(f"{obj.__class__.__name__}({obj.parameters})\n")
