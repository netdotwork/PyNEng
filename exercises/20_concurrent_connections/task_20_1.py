# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_ip_address(ip_address):
    result = subprocess.run(['ping', '-c', '5', '-n', ip_address], stdout=subprocess.DEVNULL)
    return result.returncode


def ping_ip_addresses(ip_list, limit=3):
    available_ip_list = []
    not_available_ip_list = []
    with ThreadPoolExecutor(max_workers = limit) as executor:
        result = executor.map(ping_ip_address, ip_list)
        for ip, returncodes in zip(ip_list, result):
            if returncodes == 0:
                available_ip_list.append(ip)
            else:
                not_available_ip_list.append(ip)
        return (available_ip_list, not_available_ip_list)


#testing
if __name__ == '__main__':
    ip_list1 = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses(ip_list1, limit=5))