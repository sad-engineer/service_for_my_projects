#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import pandas as pd
import sqlite3
from typing import List
from service.obj.abstract_classes import ResponseFormatter


class InPandasTableFormatter(ResponseFormatter):
    """Класс читает данные из БД в таблицу pandas.DataFrame """
    def read(self, query: str, conn: sqlite3.connect) -> pd.DataFrame:
        return pd.read_sql(query, conn)


class InListFormatter(ResponseFormatter):
    """Класс читает данные из БД !!! """
    def read(self, query: str, conn: sqlite3.connect) -> list:
        cur = conn.cursor()
        cur.execute(query)
        return cur.execute(query).fetchall()


class InListDictFormatter(ResponseFormatter):
    """Класс читает данные из БД !!! """
    def read(self, query: str, conn: sqlite3.connect) -> List[dict]:
        cur = conn.cursor()
        cur.execute(query)
        columns = [column[0] for column in cur.description]
        rows = cur.fetchall()
        data = []
        for i in range(len(rows)):
            key = i
            item = {column_name: value for column_name, value in zip(columns, rows[i])}
            data.append(item)
        return data


class InDictFormatter(ResponseFormatter):
    """Класс читает данные из БД !!! """
    def read(self, query: str, conn: sqlite3.connect) -> dict[int, dict]:
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
