# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ['duplex', 'alias', 'Current configuration']

cfg_list = []

with open('config_sw1.txt') as f:
    for line in f:
        value = False
        i = 0
        while i < 3 and not value:
            if not line.startswith(ignore[i]) and not line.startswith(' ' + ignore[i]):
                i += 1
                continue
            else:
                i = 3
                value = True
        else:
            if value == True:
                continue
            else:
                cfg_list.append(line)
                continue
f1 = open('config_sw1_cleared.txt', 'w')
f1.writelines(cfg_list)
f1.close()