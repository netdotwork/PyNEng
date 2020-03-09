# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

# use replace-method (for strings) for replace'Fast' on 'Gigabit' and print it
print(nat.replace('Fast', 'Gigabit'))