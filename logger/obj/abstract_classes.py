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
