#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .obj.abstract_classes import Dictionarer
from .obj.abstract_classes import Notifier
from .obj.abstract_classes import RecordRequester
from .obj.cataloger import Cataloger
from .obj.checker_in_dict import CheckerInDictionary
from .obj.decorators import timeit
from .obj.decorators import timeit_property
from .obj.decorators import logged
from .obj.containers import Requester
from .obj.exceptions import InvalidValue, ReceivedEmptyDataFrame
from .obj.request_record_from_sqlyte import RequestRecordFromSQLyte

__all__ = [
    # Abstractclass
    'Dictionarer',
    'Notifier',
    'RecordRequester',
    # Каталогеры
    'Cataloger',
    # Интерфейсы
    'CheckerInDictionary',
    # Декораторы
    'timeit',
    'timeit_property',
    'logged',
    # Контейнеры
    'Requester',
    # Пользовательские ошибки
    'InvalidValue',
    'ReceivedEmptyDataFrame',
    # Работа с БД
    'RequestRecordFromSQLyte',
    ]


# if __name__ == "__main__":
#
#     container = Requester()
#     requester = container.requester()
#     print(requester)
#     reader = container.reader()
#     print(reader)
#
#
#     settings = {'path': ':memory:', 'tablename': ':memory:', 'requester_type': 'sqlite', 'reader_type': 'list'}
#     container.config.from_dict(settings)
#     reader = container.reader()
#     print(reader)
#
#     settings = {'path': ':memory:', 'tablename': ':memory:', 'requester_type': 'sqlite', 'reader_type': 'list_dict'}
#     container.config.from_dict(settings)
#     reader = container.reader()
#     print(reader)
#
#     print(container.config())
