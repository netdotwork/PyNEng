# -*- coding: utf-8 -*-

"""
Задание 25.1b

Изменить класс Topology из задания 25.1a или 25.1.

Добавить метод delete_link, который удаляет указанное соединение.
Метод должен удалять и зеркальное соединение, если оно есть.

Если такого соединения нет, выводится сообщение "Такого соединения нет".

Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление линка:
In [9]: t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление зеркального линка
In [11]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))

In [12]: t.topology
Out[12]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}

Если такого соединения нет, выводится сообщение:
In [13]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
Такого соединения нет

"""


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict1):
        a = set(topology_dict1.keys())
        b = set(topology_dict1.values())
        topology_new_dict = {}
        for key in a:
            if key not in b:
                topology_new_dict.update({key: topology_dict1[key]})
        a.intersection(b)
        for c in a:
            if c not in topology_new_dict.values():
                topology_new_dict[c] = topology_dict1[c]
        return topology_new_dict

    def delete_link(self, value1, value2):
        a = list(self.topology.keys())
        b = list(self.topology.values())
        if value1 in a and value2 == self.topology[value1]:
            del self.topology[value1]
        elif value2 in a and value1 == self.topology[value2]:
            del self.topology[value2]
        else:
            print("Такого соединения нет")


#testing
if __name__ == "__main__":
    topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}
    t = Topology(topology_example)
    print(t.topology)

    t.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    print(t.topology)

    t.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))

    t.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    print(t.topology)