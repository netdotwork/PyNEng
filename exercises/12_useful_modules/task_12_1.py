# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess
#import ipaddress


def ping_ip_addresses(ip_list):
    available_ip_list = []
    not_available_ip_list = []
    for ip in ip_list:
        result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            available_ip_list.append(ip)
        else:
            not_available_ip_list.append(ip)
    tuple_1 = (available_ip_list, not_available_ip_list)
    return tuple_1


#testing
if __name__ == '__main__':
    list1 = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses(list1))