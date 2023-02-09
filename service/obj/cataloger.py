#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
class ModuleCataloger:
    """ Хранит ссылки на классы проекта, в module_name дать название модуля, в котором будем искать классы
    """
    def __init__(self, module_name: str) -> None:
        self._classes = [obj for name, obj in __import__(module_name).__dict__.items() if isinstance(obj, type)]

    @property
    def classes(self) -> list:
        return self._classes

    def get_class(self, name: str):
        return next((class_ for class_ in self._classes if name == class_.__name__), None)


class DictCataloger:
    """ Хранит ссылки на классы проекта. В classes_by_type дать словарь классов """
    def __init__(self, classes: dict) -> None:
        self._classes = classes

    @property
    def classes(self) -> list:
        return list(self._classes.values())

    def get_class(self, key: str):
        assert key in self._classes
        return self._classes[key]


if __name__ == "__main__":
    cataloger = ModuleCataloger("service.obj.terminal_printer")
    print(cataloger.classes)

