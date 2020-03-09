# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology


def create_network_map(filenames):
    '''
    Функция create_network_map обрабатывает вывод команды show cdp neighbors
    из нескольких файлов и объединяет его в одну общую топологию.

    У функции должен быть один параметр filenames (вместо него *args),
    который ожидает как аргумент список с именами файлов, в которых находится
    вывод команды show cdp neighbors.

    С помощью функции draw_topology из файла draw_network_graph.py рисуем схему на основании
    топологии, полученной с помощью функции create_network_map.

    Результат помещается в 'img/topology'
    '''

    map = {}

    key_list = []

    # открываем каждый файл как строку, формируем общий словарь из всех файлов-аргументов
    # с помощью функции parse_cdp_neighbors()
    for file in filenames:
        with open(file) as f:
            f_line = f.read()
            a = parse_cdp_neighbors(f_line)
            map.update(a)
    # проверяем полученный словарь на дублирование ключей и значений, исключаем дубли
    # всё, что дублируется, помещаем в список key_list
    for key in map.keys():
        for value in map.values():
            if key == value:
                key_list.append(key)
    # теперь удаляем из списка key_list первую половину значений (например, первые 3 из списка из 6 значений)
    # т.к. нужно удалить только дублирующиеся значения, а не все повторяющиеся
    for i in range(0, int((len(key_list))/2)):
        key_list.pop(0)
    for key1 in key_list:
        del map[key1]
    # рисуем топологию в 'img/topology'
    draw_topology(map)
    return map

# testing
if __name__ == '__main__':
    filenames1 = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
    create_network_map(filenames1)