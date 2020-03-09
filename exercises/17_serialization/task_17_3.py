# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re
from pprint import pprint


def parse_sh_cdp_neighbors(sh_cdp_ne_line):
    '''
    sh_cdp_ne_line - вывод команды show cdp neighbors в виде строки
    '''
    regex_0 = (r'(\w+\d+)\s+(\w+ \d+/\d+).*?(\w+ \d+/\d+)')
    regex = (r'(\w+)>')
    device = re.search(regex, sh_cdp_ne_line)
    new_dict = {device.group(1): {}}
    for peer in re.finditer(regex_0, sh_cdp_ne_line, re.DOTALL):
        new_dict[device.group(1)][peer.group(2)] = {peer.group(1): peer.group(3)}
    return new_dict

#testing
if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))