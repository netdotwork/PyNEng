# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = '''
Protocol:              {0}
Prefix:                {1}
AD/Metric:             {2}
Next-Hop:              {4}
Last update:           {5}
Outbound Interface:    {6}
'''

with open('ospf.txt') as f:
    for file in f:
        list = file.split()
        print(template.format(list[0], list[1], list[2].strip('[]'), list[3], list[4], list[5], list[6]).rstrip())