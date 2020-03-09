# -*- coding: utf-8 -*-

"""
Задание 26.1a

В этом задании надо сделать так, чтобы экземпляры класса Topology были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 25.1x или задания 26.1.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""

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


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        self.topology1 = topology_dict
        self._a = list(self.topology1.keys())
        self._b = list(self.topology1.values())

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

    def __iter__(self):
        return zip(self._a, self._b)

    #def __add__(self, other):
    #    topology3 = {}
    #    for key, value in self.topology1.items():
    #        topology3[key] = value
    #    topology3.update(other)
    #    return Topology(topology3)


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

    top = Topology(topology_example)
    print(top, end = '\n\n')

    for link in top:
        print(link)