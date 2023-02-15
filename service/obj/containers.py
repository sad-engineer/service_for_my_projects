#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import sqlite3
from dependency_injector import containers, providers

from service.obj.request_record_from_sqlyte import RequestRecordFromSQLyte
from service.obj.request_formatters import InPandasTableFormatter
from service.obj.request_formatters import InListFormatter
from service.obj.request_formatters import InListDictFormatter
from service.obj.request_formatters import InDictFormatter


class Requester(containers.DeclarativeContainer):

    config = providers.Configuration()

    # База данных для запросов
    database_client = providers.Singleton(
        sqlite3.connect,
        config.path,
    )

    # Ридеры данных из БД:
    to_pandas_table = providers.Singleton(
        InPandasTableFormatter,
    )

    to_list = providers.Singleton(
        InListFormatter,
    )

    to_list_dict = providers.Singleton(
        InListDictFormatter,
    )

    to_dict = providers.Singleton(
        InDictFormatter,
    )

    # Выбор класса чтения данных
    reader = providers.Selector(
        config.reader_type,
        pandas_table=to_pandas_table,
        list=to_list,
        list_dict=to_list_dict,
        dict=to_dict,
    )

    # Классы запросов:
    csv_requester = providers.Singleton()

    sqlyte_requester = providers.Factory(
        RequestRecordFromSQLyte,
        tablename=config.tablename,
        database_client=database_client,
        database_reader=reader
    )

    # Выбор класса запросов
    requester = providers.Selector(
        config.requester_type,
        csv=csv_requester,
        sqlite=sqlyte_requester,
    )
