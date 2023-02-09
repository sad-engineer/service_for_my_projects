#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
class Cataloger:
    """ Хранит ссылки на классы проекта"""
    def __init__(self, module_name: str, dict_types: dict) -> None:
        self._classes = [obj for name, obj in __import__(module_name).__dict__.items() if isinstance(obj, type)]
        self._dict_types = dict_types

    @property
    def classes(self) -> list:
        return self._classes

    def by_name(self, name: str):
        return next((class_ for class_ in self._classes if name == class_.__name__), None)

    def by_type(self, type_tool: str):
        assert type_tool in self._dict_types
        return self.by_name(self._dict_types[type_tool])
