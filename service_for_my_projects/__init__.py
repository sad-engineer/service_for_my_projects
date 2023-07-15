#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service_for_my_projects.obj.abstract_classes import Dictionarer
from service_for_my_projects.obj.abstract_classes import Notifier
from service_for_my_projects.obj.abstract_classes import RecordRequester
from service_for_my_projects.obj.cataloger import Cataloger
from service_for_my_projects.obj.checker_in_dict import CheckerInDictionary
from service_for_my_projects.obj.decorators import timeit
from service_for_my_projects.obj.decorators import timeit_property
from service_for_my_projects.obj.decorators import logged
from service_for_my_projects.obj.decorators import output_debug_message_for_init_method
from service_for_my_projects.obj.containers import Requester
from service_for_my_projects.obj.exceptions import CreationError, InvalidValue, InvalidTypeValue, ReceivedEmptyDataFrame, InvalidModuleName
from service_for_my_projects.obj.request_record_from_sqlyte import RequestRecordFromSQLyte

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
