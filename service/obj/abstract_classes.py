#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod


class Dictionarer(ABC):
    """ Абстрактный класс, наследовать для вывода словаря параметров класса"""

    @abstractmethod
    def _parameters(self) -> dict: pass
    # """ Возвращать словарь публичных параметров класса. Использовать для конструктора внутри дочерних классов
    # (при множественном наследовании) """

    @property
    def parameters(self):
        return self._parameters()


class Notifier(ABC):
    """ Абстрактный класс, базовый для всех логеров или классов вывода результата"""
    @abstractmethod
    def log(self, obj, message, path, full): return path


class RecordRequester(ABC):
    """ Абстрактный класс, реализующий работу с какой-либо БД"""

    @abstractmethod
    # Реализация метода должна обеспечивать получение записей по словарю столбцов:значений, передаваемых в
    # values_dict
    def get_records(self, values_dict: dict): pass

    @property
    @abstractmethod
    # Возвращает DataFrame со всеми записями таблицы tablename.
    def get_all_records(self): pass


class DatabaseReader(ABC):
    """ Абстрактный класс, должен содержать функционал формата чтения данных из БД (в каком формате возвращать данные)
    """
    @abstractmethod
    # Возвращает данные в своем формате.
    def read(self, query, conn): pass
