#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import sqlite3
from typing import Any

from service.obj.abstract_classes import RecordRequester, ResponseFormatter


class RequestRecordFromSQLyte(RecordRequester):
    """Класс запросов для работы с таблицами в базе данных SQLyte.
    Необходимо передать подключение к базе данных (database_client: sqlite3.Connection), имя таблицы (tablename: str)
    в этой БД и класс, определяющий формат выводимых данных (database_reader: DatabaseReader)
    """
    def __init__(self, tablename: str, database_client: sqlite3.Connection, database_reader: ResponseFormatter):
        """Инициализация объекта"""
        self.tablename = tablename
        self._database_client = database_client
        self._database_reader = database_reader

    def get_records(self, compliance_criteria: dict) -> Any:
        """
        Возвращает записи по критерию отбора, который передан в словаре compliance_criteria.
        Выдаст строки в которых, столбцы compliance_criteria.keys содержат соответствующие
        compliance_criteria.values

        Parameters:
        compliance_criteria : dict : Словарь с именами столбцов в качестве ключей и значениями в качестве значений.

        Возвращает
        -------
            Строки, в которых столбцы содержат соответствующие и значения. Тип возвращаемых данных определяет
            self._database_reader.
        """
        with self._database_client as conn:
            query = f"SELECT * FROM {self.tablename} WHERE "
            for column, value in compliance_criteria.items():
                query += f"{column} = '{value}' AND "
            query = query[:-4]
        return self._database_reader.read(query, conn)

    @property
    def get_all_records(self) -> Any:
        """ Возвращает все записи таблицы self.tablename. Тип возвращаемых данных определяет self._database_reader."""
        with self._database_client as conn:
            query = f"SELECT * FROM {self.tablename}"
        return self._database_reader.read(query, conn)

    def available_values(self) -> dict:
        """ Возвращает наборы доступных в таблице БД значений по категориям."""
        result = {}
        with self._database_client as conn:
            cursor = conn.cursor()
            cursor.execute(f'PRAGMA table_info({self.tablename}))')
            columns = cursor.fetchall()
            for column in columns:
                cursor.execute(f"SELECT {column[1]} FROM {self.tablename}")
                result[column[1]] = set(cursor.fetchall())
        return result
