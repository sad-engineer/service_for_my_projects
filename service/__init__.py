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
from .obj.decorators import output_debug_message_for_init_method
from .obj.containers import Requester
from .obj.exceptions import CreationError, InvalidValue, InvalidTypeValue, ReceivedEmptyDataFrame, InvalidModuleName
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
    'output_debug_message_for_init_method',
    # Контейнеры
    'Requester',
    # Пользовательские ошибки
    'CreationError',
    'InvalidModuleName',
    'InvalidValue',
    'InvalidTypeValue',
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
