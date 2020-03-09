# -*- coding: utf-8 -*-

"""
Задание 26.1

Изменить класс Topology из задания 25.1x.

Добавить метод, который позволит выполнять сложение двух объектов (экземпляров) Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

Создание двух топологий:

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Суммирование топологий:

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка, что исходные топологии не изменились:

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
"""


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        self.topology1 = topology_dict

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
    # в методе __add__ аргумент other, по умолчанию, не является итерируемым объектом (это объект класса Topology, не итерируемый);
    # необходимо добавить метод __iter__ для того, чтобы при обращении к other как к итерируемому объекту возвращались значения из итератора,
    # созданного функцией iter
    # в данном случае, мы возвращаем итератор уже итерируемого объекта, т.к. у нас есть подходящий итерируемый объект
    # в противном случае, мы могли бы сделать экземпляр нашего класса Topology итератором с помощью специального метода __next__
    def __iter__(self):
        return iter(self.topology1.items())

    def __add__(self, other):
        topology3 = {}
        for key, value in self.topology1.items():
            topology3[key] = value
        topology3.update(other)
        return Topology(topology3)


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

    topology_example2 = {
    ("R1", "Eth0/4"): ("R7", "Eth0/0"),
    ("R1", "Eth0/6"): ("R9", "Eth0/0"),
}

    t1 = Topology(topology_example)
    print(t1.topology, end = '\n\n')

    t2 = Topology(topology_example2)
    print(t2.topology, end = '\n\n')

    #print(t1+t2)

    t3 = t1+t2
    print(t3.topology, end = '\n\n')

    print(t1.topology, end = '\n\n')

    print(t2.topology, end = '\n\n')