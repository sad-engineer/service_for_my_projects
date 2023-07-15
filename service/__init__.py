#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service.obj.abstract_classes import Dictionarer
from service.obj.abstract_classes import Notifier
from service.obj.abstract_classes import RecordRequester
from service.obj.cataloger import Cataloger
from service.obj.checker_in_dict import CheckerInDictionary
from service.obj.decorators import timeit
from service.obj.decorators import timeit_property
from service.obj.decorators import logged
from service.obj.decorators import output_debug_message_for_init_method
from service.obj.containers import Requester
from service.obj.exceptions import CreationError, InvalidValue, InvalidTypeValue, ReceivedEmptyDataFrame, InvalidModuleName
from service.obj.request_record_from_sqlyte import RequestRecordFromSQLyte

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
#     container = Requester()
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
