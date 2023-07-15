#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CreationError(Exception):
    """Исключение выбрасывать при ошибке создания экземпляра класса.

    Parameters:
        message: str : объяснение ошибки
    """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class InvalidValue(Exception):
    """Исключение возникает при некорректном значении переменной. Например, если значение пустое

    Parameters:
        message: str : объяснение ошибки
    """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class InvalidTypeValue(Exception):
    """Исключение возникает при некорректном значении типа переменной. Например, если значение не соответствует
    ожидаемому типу

    Parameters:
        message: str : объяснение ошибки
    """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class ReceivedEmptyDataFrame(Exception):
    """Выкидывать ошибку, если DataFrame пустой.

    Parameters:
        message: str : объяснение ошибки
    """
    def __init__(self, message="") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidModuleName(Exception):
    """Выкидывать ошибку, если модуль не существует.

    Parameters:
        message: str : объяснение ошибки
    """
    def __init__(self, message="") -> None:
        self.message = message
        super().__init__(self.message)
