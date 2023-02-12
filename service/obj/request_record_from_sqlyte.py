#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import pandas as pd
import sqlite3

from service.obj.abstract_classes import RecordRequester, DatabaseReader


class ReaderInPandasTable(DatabaseReader):
    """Класс читает данные из БД в таблицу pandas.DataFrame """
    def read(self, query, conn):
        return pd.read_sql(query, conn)


class ReaderInList(DatabaseReader):
    """Класс читает данные из БД !!! """
    def read(self, query, conn):
        cur = conn.cursor()
        cur.execute(query)
        return cur.execute(query).fetchall()


class ReaderInListDict(DatabaseReader):
    """Класс читает данные из БД !!! """
    def read(self, query, conn):
        cur = conn.cursor()
        cur.execute(query)
        columns = [column[0] for column in cur.description]
        rows = cur.fetchall()
        data = []
        for i in range(len(rows)):
            key = i
            item = {column_name: value for column_name, value in zip(columns, rows[i])}
            data[key] = item
        return data


class ReaderInDict(DatabaseReader):
    """Класс читает данные из БД !!! """
    def read(self, query, conn):
        cur = conn.cursor()
        cur.execute(query)
        columns = [column[0] for column in cur.description]
        rows = cur.fetchall()
        data = {}
        for i in range(len(rows)):
            key = i
            item = {column_name: value for column_name, value in zip(columns, rows[i])}
            data[key] = item
        return data


class RequestRecordFromSQLyte(RecordRequester):
    """Класс запросов для работы с таблицами в базе данных SQLyte."""

    def __init__(self, tablename: str, database_client: sqlite3.Connection, database_reader):
        """Инициализация объекта"""
        self.tablename = tablename
        self._database_client = database_client
        self._database_reader = database_reader

    def get_records(self, values_dict: dict) -> pd.DataFrame:
        """
        Возвращает DataFrame с записями, которые соответствуют данным столбцам и значениям.

        Параметры
        ----------
        values_dict : dict
            Словарь с именами столбцов в качестве ключей и значениями в качестве значений.

        Возвращает
        -------
        DataFrame
            DataFrame с записями, соответствующими данным столбцам и значениям.
        """
        with self._database_client as conn:
            query = f"SELECT * FROM {self.tablename} WHERE "
            for column, value in values_dict.items():
                query += f"{column} = '{value}' AND "
            query = query[:-4]
        return self._database_reader.read(query, conn)

    @property
    def get_all_records(self) -> pd.DataFrame:
        """ Возвращает DataFrame со всеми записями таблицы tablename."""
        with self._database_client as conn:
            query = f"SELECT * FROM {self.tablename}"
        return self._database_reader.read(query, conn)
