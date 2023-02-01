#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import datetime
import os

from logger.obj.abstract_classes import Notifier
from typing import ClassVar


class StandardResultFilePrinter(Notifier):
    """ Класс вывода полей объекта в файл logs\\{data_key}_log.txt,
     где data_key - метка времени создания файла
    """
    DECODING: ClassVar[dict] = {}

    def __init__(self) -> None:
        # Настройки по умолчанию. Расположение лога определять вне класса.
        self.prefix = datetime.datetime.now().strftime('%H-%M %d-%m-%Y')
        self.folder = os.path.join(os.getcwd(), "logs")
        self.path = self.folder + f"\\{self.prefix}_log.txt"

    def _check_folder(self, folder_path=None) -> None:
        """ Если папки 'logs' в директории проекта нет - создаст ее.
        """
        if isinstance(folder_path, type(None)):
            folder_path = self.folder
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    def log(self, obj, message=None, path=None, full=False) -> str:
        """ У логируемого объекта 'obj' ловит словарь параметров и свойств ('obj' должен иметь метод
        'parameters'), печатает описание и значение ключа (описание берет из словаря 'DECODING'). Для печати
        ключей, для которых описание не определено в 'DECODING', задать full=True.
        """
        if isinstance(path, type(None)):
            self._check_folder()
            path = self.path

        with open(path, 'a+', encoding='UTF8') as f:
            f.write(f"{message}\n")
            for key, val in obj.parameters.items():
                if full:
                    f.write(f"{self.DECODING[key].format(obj=val)}\n") if key in self.DECODING else \
                        f.write(f"{key} = {val}\n")
                else:
                    f.write(f"{self.DECODING[key].format(obj=val)}\n") if key in self.DECODING else f.write(f"")
            f.write("\n")
        return path


class StandardObjectFilePrinter(StandardResultFilePrinter):
    """ Класс вывода объекта в файл logs\\{data_key}_log.txt, где data_key - метка времени создания файла"""
    def __init__(self):
        StandardResultFilePrinter.__init__(self)

    def log(self, obj, message=None, path=None, _full=False):
        """ У логируемого объекта 'obj' ловит словарь параметров и свойств ('obj' должен иметь метод
        'parameters'), печатает название класса и словарь параметров.
        """
        if isinstance(path, type(None)):
            self._check_folder()
            path = self.path

        with open(path, 'a+', encoding='UTF8') as f:
            f.write(f"{obj.__class__.__name__}({obj.parameters})\n")
        return path


class StandardObjectFileSaver(StandardResultFilePrinter):
    """ Класс вывода объекта в файл logs\\{data_key}_log.txt. Выводит только поля, заданные в SAVED_FIELDS"""
    SAVED_FIELDS: ClassVar[list] = []

    def __init__(self):
        StandardResultFilePrinter.__init__(self)

    def log(self, obj, message=None, path=None, _full=False):
        """ У логируемого объекта 'obj' ловит словарь параметров и свойств ('obj' должен иметь метод
        'parameters'), печатает название класса и словарь параметров.
        """
        if isinstance(path, type(None)):
            self._check_folder()
            path = self.path

        with open(path, 'a+', encoding='UTF8') as f:
            parameters = {k: obj.parameters.get(k) for k in self.SAVED_FIELDS if obj.parameters.get(k) is not None}
            f.write(f"{obj.__class__.__name__}({parameters})\n")
        return path
