# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = '192.168.3.1'

# transform string-type to list-type (separator '.')
ip1 = ip.split('.')

# form template for new string (0,1,2,3 - numbers of arguments from our list,
# <010b - 10 numbers in binary format + padding with 0)
ip_template = '''
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<010b} {1:<010b} {2:<010b} {3:<010b}
'''

# output of our template and trasnform strings from list to int-type
print(ip_template.format(int(ip1[0]), int(ip1[1]), int(ip1[2]), int(ip1[3])))