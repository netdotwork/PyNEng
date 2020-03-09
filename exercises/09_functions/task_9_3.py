# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    '''
    Функция отображает набор интерфейсов и настроенных vid в виде кортежа из словарей.
    Для access-интерфейсов выводит все vid, не включая 1.
    Для trunk-интерфейсов выводит vid в виде списка значений
    '''
    interface_list = []

    access_dict = {}

    trunk_dict = {}

    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if line.startswith('interface F'):
                key = line.lstrip('interface')
            elif line.startswith(' switchport access'):
                access_dict.update({key.strip(): int(line[23::].strip())})
            elif line.startswith(' switchport trunk allowed'):
                trunk_dict.update({key.strip(): [int(i) for i in line[30::].split(',')]})
        return(tuple([access_dict, trunk_dict]))

#testing
print(get_int_vlan_map('config_sw1.txt'))