# -*- coding: utf-8 -*-
"""
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"

# transform our string-type to list-type (with separator ':')
mac1 = mac.split(':')

# change separator ':' to '.' and print it
# use .format-method and arguments of list to form a new string
print("{}.{}.{}".format(mac1[0], mac1[1], mac1[2]))
# alternative version
print('.'.join(mac1))
# alternative version
print(mac.replace(':', '.'))