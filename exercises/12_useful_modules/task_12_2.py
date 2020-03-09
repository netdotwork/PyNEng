# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_to_ip_list(ip_list):
    convert_ip_list = []
    for ip in ip_list:
        try:
            ipaddress.ip_address(ip)
            convert_ip_list.append(str(ipaddress.ip_address(ip)))
        except ValueError:
            ip_list1 = ip.split('-')
            if '.' in ip_list1[1]:
                ip_list2 = ip_list1[0].split('.')
                ip_list3 = ip_list1[1].split('.')
                for i in range(int(ip_list2[3]), int(ip_list3[3])+1):
                    convert_ip_list.append(str(ipaddress.ip_address(f'{ip_list2[0]}.{ip_list2[1]}.{ip_list2[2]}.{i}')))
            else:
                ip_list2 = ip_list1[0].split('.')
                for i in range(int(ip_list2[3]), int(ip_list1[1])+1):
                    convert_ip_list.append(str(ipaddress.ip_address(f'{ip_list2[0]}.{ip_list2[1]}.{ip_list2[2]}.{i}')))
    return convert_ip_list

#testing
if __name__ == '__main__':
    list1 = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(list1))