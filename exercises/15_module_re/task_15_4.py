# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re


def get_ints_without_description(filename):
    # убираем жадность символов повторения с помощь ? после символов повторения, т.к. в файле много !
    regex = ('\ninterface (\S+).+?!')
    interface_list = []
    with open(filename) as f:
    # с помощью флага re.DOTALL делаем так, чтобы символ переноса строки '\n' не ограничивал регулярное выражение .+
        for ip in re.finditer(regex, f.read(), re.DOTALL):
            if 'description' in ip.group(0):
                continue
            else:
                interface_list.append(f'{ip.group(1)}')
        return interface_list

#testing
if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))