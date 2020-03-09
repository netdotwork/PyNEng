# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

r_file = str(argv[1])
w_file = str(argv[2])
cfg_list = []
with open(r_file) as f:
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
f1 = open(w_file, 'w')
f1.writelines(cfg_list)
f1.close()