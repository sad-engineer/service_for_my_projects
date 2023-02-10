#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import sqlite3
from dependency_injector import containers, providers

from service.obj.request_record_from_sqlyte import RequestRecordFromSQLyte
from service.obj.request_record_from_sqlyte import ReaderInPandasTable
from service.obj.request_record_from_sqlyte import ReaderInList
from service.obj.request_record_from_sqlyte import ReaderInListDict

SETTINGS = {'path': ':memory:', 'tablename': ':memory:', 'requester_type': 'sqlite', 'reader_type': 'pandas_table'}


class Requester(containers.DeclarativeContainer):

    config = providers.Configuration()
    config.from_dict(SETTINGS)

    # База данных для запросов
    database_client = providers.Singleton(
        sqlite3.connect,
        config.path,
    )

    # Ридеры данных из БД:
    to_pandas_table = providers.Singleton(
        ReaderInPandasTable,
    )

    to_list = providers.Singleton(
        ReaderInList,
    )

    to_list_dict = providers.Singleton(
        ReaderInListDict,
    )

    # Выбор класса чтения данных
    reader = providers.Selector(
        config.reader_type,
        pandas_table=to_pandas_table,
        list=to_list,
        list_dict=to_list_dict,
    )

    # Классы запросов:
    csv_requester = providers.Singleton()

    sqlyte_requester = providers.Singleton(
        RequestRecordFromSQLyte,
        tablename="tools",
        database_client=database_client,
        database_reader=reader
    )

    # Выбор класса запросов
    requester = providers.Selector(
        config.requester_type,
        csv=csv_requester,
        sqlite=sqlyte_requester,
    )


