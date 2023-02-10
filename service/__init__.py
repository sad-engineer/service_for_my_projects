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
    # Пользовательские ошибки
from service.obj.exceptions import InvalidValue, ReceivedEmptyDataFrame
    # Вывод в файл
from service.obj.file_printer import StandardResultFilePrinter
from service.obj.file_printer import StandardObjectFilePrinter
from service.obj.file_printer import StandardObjectFileSaver
    # Logger`ы
from service.obj.loggerer import Logger
    # Работа с БД
from service.obj.request_record_from_sqlyte import RequestRecordFromSQLyte
    # Вывод в консоль
from service.obj.terminal_printer import StandardResultTerminalPrinter
from service.obj.terminal_printer import StandardObjectTerminalPrinter


from service.obj.containers import Requester


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
