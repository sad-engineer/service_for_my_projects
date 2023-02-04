#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import os
import sqlite3
from dependency_injector import containers, providers
# from dependency_injector.wiring import Provide, inject

from logger.obj import cataloger, exceptions, file_printer, constants, loggerer, request_record_from_sqlyte, \
    terminal_printer


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.databases.local_database.from_value(':memory:')

    # Gateways
    local_database_client = providers.Singleton(
        sqlite3.connect,
        config.databases.local_database,
    )

    # Services
    cataloger = providers.Singleton(
        cataloger.Cataloger,
        module_names=["logger", ],
    )

    invalid_value = providers.Singleton(
        exceptions.InvalidValue,
        message=""
    )

    standard_result_file_printer = providers.Singleton(
        file_printer.StandardResultFilePrinter,
        decoding=constants.DECODING,
    )

    standard_object_file_printer = providers.Singleton(
        file_printer.StandardResultFilePrinter,
        decoding=constants.DECODING,
    )

    standard_object_file_saver = providers.Singleton(
        file_printer.StandardObjectFileSaver,
        decoding=constants.DECODING,
    )

    logger = providers.Singleton(
        loggerer.Logger
    )

    request_record_from_sqlyte = providers.Singleton(
        request_record_from_sqlyte.RequestRecordFromSQLyte,
        filename="",
        tablename=""
    )

    standard_result_terminal_printer = providers.Singleton(
        terminal_printer.StandardResultTerminalPrinter,
        decoding=constants.DECODING,
    )

    standard_object_terminal_printer = providers.Singleton(
        terminal_printer.StandardObjectTerminalPrinter,
    )


if __name__ == "__main__":
    ct = Container()

    # requester = ct.requester()
    # print(requester.filename)
    # print(requester.tablename)

    # finder = ct.finder()
    # table = finder.find_all
    # print(table)

    # cataloger = ct.cataloger()
    # print(cataloger.classes)

    creator = ct.creator_from_log_line
    with open(os.getcwd().replace('obj', 'logs\\log.txt'), mode='r', encoding="utf8") as f:
        context = f.readlines()
    for line in context:
        cutter = creator().create(log_line=line)
        print(cutter)
        print(cutter.name)

    cutter = ct.drilling_cutter()
    print(cutter.length_mm)

    ct.drilling_cutter.reset()
    cutter = ct.drilling_cutter(length_mm=16)
    print(cutter.length_mm)

    ct.drilling_cutter.reset()
    cutter = ct.drilling_cutter()
    print(cutter.length_mm)

    cutter.length_mm = 40
    print(cutter.length_mm)
    print(cutter.__class__.__name__)
