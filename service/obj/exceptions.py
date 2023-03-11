#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InvalidValue(Exception):
    """Исключение возникает при некорректном значении переменной.
    Например, если значение пустое

    Атрибуты:
        message: объяснение ошибки
    """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class ReceivedEmptyDataFrame(Exception):
    """Выкидывать ошибку, если DataFrame пустой.

    Атрибуты:
        message: объяснение ошибки
    """
    def __init__(self, message="") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidTypeValue(Exception):
    """Исключение возникает при некорректном значении типа переменной.
    Например, если значение не соответствует ожидаемому типу

    Атрибуты:
        message: объяснение ошибки
    """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)
