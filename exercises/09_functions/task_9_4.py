# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    # сложно
    #for list_command in ignore:
    #    if list_command in str(command):
    #        return True
    #        break
    #    else:
    #        continue
    #else:
    #    return False

    # проще
    #for word in ignore:
    #    if word in command:
    #        return True
    #return False

    # очень просто
    return any(word in command for word in ignore)

from pprint import pprint

def convert_config_to_dict(config_filename):
    '''
    Функция проверяет файл конфигурации построчно.
    Исключает строки, совпадающие со значениями списка ignore, даже частично.
    Выводит в виде словаря
    '''
    config_dict = {}

    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if ignore_command(line, ignore) or line[0] == '!' or line == '\n':
                continue
            elif line[0] != ' ':
                key = line.strip()
                config_dict[key] = []
                continue
            elif line[0] == ' ':
                config_dict[key].append(line.strip())
        return config_dict


# testing
pprint(convert_config_to_dict('config_sw1.txt'))