# -*- coding: utf-8 -*-
"""
Задание 4.4

Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров. Для получения итогового списка нельзя удалять конкретные
vlanы вручную.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

# transform our list-type to tuple-type for detect unique arguments only
set1 = set(vlans)

# transform back (we have got unique list of elements already)
# sort and print it
list1 = list(set1)
list1.sort()
print(list1)