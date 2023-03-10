#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Классы пакета
    # Abstractclass
from service.obj.abstract_classes import Dictionarer
from service.obj.abstract_classes import Notifier
from service.obj.abstract_classes import RecordRequester
    # Каталогеры
from service.obj.cataloger import Cataloger
    # Интерфейсы
from service.obj.checker_in_dict import CheckerInDictionary
    # Декораторы
from service.obj.decorators import timeit
from service.obj.decorators import timeit_property
from service.obj.decorators import logged
    # Контейнеры
from service.obj.containers import Requester
    # Пользовательские ошибки
from service.obj.exceptions import InvalidValue, ReceivedEmptyDataFrame
    # Работа с БД
from service.obj.request_record_from_sqlyte import RequestRecordFromSQLyte


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
