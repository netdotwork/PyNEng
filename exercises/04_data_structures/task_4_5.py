# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

# keep only numbers and transform strings to list-type (with ',' separator)
command3 = command1[30:].split(',')
command4 = command2[30:].split(',')

# transform our lists to tuple-type
set1 = set(command3)
set2 = set(command4)

# find similar numbers in our tuples
duplicate_set = set1.intersection(set2)
#print(duplicate_set)

# transform tuple to list and sort it
list1 = list(duplicate_set)
list1.sort()

# output
print(list1)