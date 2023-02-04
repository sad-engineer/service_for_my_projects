#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import sqlite3
from dependency_injector import containers, providers
# from dependency_injector.wiring import Provide, inject

from logger.obj import cataloger, exceptions, file_printer, constants, loggerer, request_record_from_sqlyte, \
    terminal_printer

PATH_DB_FOR_TOOLS = f"{__file__}".replace("obj\\containers.py", "data\\cutting_tools.db")


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.databases.local_database.from_value(':memory:')
    config.databases.database_for_tools.from_value(PATH_DB_FOR_TOOLS)

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
        saved_fields=[],
    )

    logger = providers.Singleton(
        loggerer.Logger
    )

    request_record_from_sqlyte = providers.Factory(
        request_record_from_sqlyte.RequestRecordFromSQLyte,
        database_client=local_database_client,
        tablename="cutting_tools"
    )

    standard_result_terminal_printer = providers.Singleton(
        terminal_printer.StandardResultTerminalPrinter,
        decoding=constants.DECODING,
    )

    standard_object_terminal_printer = providers.Singleton(
        terminal_printer.StandardObjectTerminalPrinter,
    )
