# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = 'AAAA:BBBB:CCCC'

# transform string-type to list-type (separator ':')
mac1 = mac.split(':')

# transform back from list-type to string-type (without separator)
mac2 = ''.join(mac1)

# trasnform string-type to int-type and binary (AAAABBBBCCCC - 16)
int1 = bin(int(mac2, 16))

# print number int1 and delete 0b
print(int1.strip('0b'))
# alternative version
print((bin(int(mac2, 16)).strip('0b')))