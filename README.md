# `logger`

`logger` - модуль логирования объектов для моих проектов.
---
---
Поддерживаемые константы:

    Пример словаря описаний полей объекта:
        logger.DECODING

---
Поддерживаемые классы:
    
    Абстрактный базовый класс для наследования всеми объектами логирования:
        logger.Dictionarer
    


    Абстрактный базовый класс для наследования всеми логгерами:
        logger.Notifier



    Класс вывода полей объекта в консоль (наследник logger.Notifier):
        создаем логер:
            terminal_printer = logger.StandardResultTerminalPrinter()
        
        задаем описание полей объекта
            terminal_printer.DECODING = any_dict
        
        вывод полей объекта
            terminal_printer.log(obj)
    


    Класс вывода объекта в консоль (наследник logger.Notifier):
        создаем логер:
            terminal_printer = logger.StandardObjectTerminalPrinter()

        вывод полей объекта
            terminal_printer.log(obj) 
    


    # частный случай логирования - лог в файл
    Класс вывода полей объекта в файл (наследник logger.Notifier):
        Создаем логер:
            file_printer = logger.StandardResultFilePrinter()
        
        Задаем описание полей объекта:
            file_printer.DECODING = any_dict
        
        Вывод полей объекта:
            # Выводит только поля, ключи которых есть в file_printer.DECODING
            file_printer.log(obj)

        Вывести все поля объекта:  
            file_printer.log(obj, full=True)

        Печать сообщения any_message перед полями объекта:  
            file_printer.log(obj, message=any_message)

        Печать объекта по пути any_path:  
            file_printer.log(obj, path=any_path) 
    


    # частный случай логирования - лог в файл
    Класс вывода объекта в файл (наследник logger.StandardResultFilePrinter):
        Создаем логер:
            file_printer = logger.StandardObjectFilePrinter()
                
        Вывод строки вида "ClassName({dict_param})" в файл:
            file_printer.log(obj)


    Класс сохранения обьекта в файл:
        Создаем логер:
            file_printer = logger.StandardObjectFileSaver()
        Сохраняет только те поля, которые указаны в свойстве "SAVED_FIELDS" класса
            file_printer. SAVED_FIELDS = ["name_1", "name_2", ...]
        Вывод строки вида "ClassName({dict_param})" в файл:
            file_printer.log(obj)

    
    `Общий класс логирования объекта:`
        создаем логер:
            printer = logger.logger(obj:Dictionarer,  notifier=any_notifier,  message=any_message,  
                                    path=any_path, full=False)
        
        вывод полей объекта в консоль (описание полей обьекта в any_dict):
            any_message = "any_message"
            terminal_printer = logger.StandardResultTerminalPrinter()
            terminal_printer.DECODING = any_dict 
            printer.log(obj:Dictionarer,  notifier=terminal_printer,  message=any_message)
        
        вывод всех полей объекта в консоль:
            any_message = "any_message"
            terminal_printer = logger.StandardResultTerminalPrinter()
            terminal_printer.DECODING = any_dict 
            printer.log(obj:Dictionarer,  notifier=terminal_printer,  message=any_message, full=True)
        
        вывод объекта в консоль:
            terminal_printer = logger.StandardObjectTerminalPrinter()
            printer.log(obj:Dictionarer,  notifier=terminal_printer)

        вывод полей объекта в файл (описание полей обьекта в any_dict):
            any_message = "any_message"
            any_path = "log.txt"
            file_printer = logger.StandardResultFilePrinter()
            file_printer.DECODING = any_dict 
            printer.log(obj:Dictionarer,  notifier=file_printer,  message=any_message, path=any_path)
        
        вывод всех полей объекта в файл:
            any_message = "any_message"
            any_path = "log.txt"
            file_printer = logger.StandardResultFilePrinter()
            file_printer.DECODING = any_dict 
            printer.log(obj:Dictionarer,  notifier=file_printer,  message=any_message, path=any_path, full=True)
        
        вывод объекта в файл:
            file_printer = logger.StandardObjectFilePrinter()
            file_printer.DECODING = any_dict
            printer.log(obj:Dictionarer,  notifier=file_printer)
        
        сохранение объекта в файл:
            file_printer = logger.StandardObjectFileSaver()
            file_printer.SAVED_FIELDS = ["name_1", "name_2", ...]    # Задаем названия полей для сохранения
            printer.log(obj:Dictionarer,  notifier=file_printer)
---
