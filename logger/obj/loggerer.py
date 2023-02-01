#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
from logger.obj.terminal_printer import StandardResultTerminalPrinter as _Terminal


class Logger:
    """ Передает в конкретный логер объект вывода """
    @staticmethod
    def log(obj, notifier=_Terminal, message=None, path=None, full=False):
        return notifier().log(obj, message, path, full)
