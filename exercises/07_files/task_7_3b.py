# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = input('Please enter vlan id: ')

line_list1 = []

with open('CAM_table.txt') as f:
    mac_table_list = f.readlines()
    for line in mac_table_list[6:]:
        line_list = line.split()
        line_list1.append([int(line_list[0]), line_list[1], line_list[3]])
    for line1 in line_list1:
        if line1[0] == int(vlan):
            print(f'{line1[0]:<4}     {line1[1]}      {line1[2]}')