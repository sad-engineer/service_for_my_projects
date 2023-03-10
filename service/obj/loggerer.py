#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import logging
from service.obj.terminal_printer import StandardResultTerminalPrinter as _Terminal


class Logger:
    """ Передает в конкретный логер объект вывода """
    @staticmethod
    def log(obj, notifier=_Terminal, message=None, path=None, full=False):
        return notifier.log(obj, message, path, full)


class BaseServiceLogger:
    """ Передает в конкретный логер объект вывода """
    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )