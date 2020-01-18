# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess
import ipaddress

available_ip_list = []
not_available_ip_list = []


def ping_ip_addresses(*args):
    for ip in args:
        result = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            available_ip_list.append(ip)
        else:
            not_available_ip_list.append(ip)
    tuple1 = (available_ip_list, not_available_ip_list)
    print(tuple1)
    return tuple1


#testing
list1 = ['192.168.0.103', '192.168.0.104', '192.168.0.1', '192.168.0.5']
ping_ip_addresses(*list1)