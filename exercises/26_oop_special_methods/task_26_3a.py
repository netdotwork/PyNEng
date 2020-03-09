# -*- coding: utf-8 -*-

"""
Задание 26.3a

Изменить класс IPAddress из задания 26.3.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

Для этого задания нет теста!
"""
class IPAddress:
    def __init__(self, ip_mask):
        for i in ip_mask.split('/')[0].split('.'):
            if int(i) >= 0 and int(i) <= 255 and len(ip_mask.split('/')[0].split('.')) == 4:
                continue
            else:
                raise ValueError("Incorrect IPv4 address")
                break
        else:
            self.ip = ip_mask.split('/')[0]
        if int(ip_mask.split('/')[1]) >= 8 and int(ip_mask.split('/')[1]) <= 32:
            self.mask = int(ip_mask.split('/')[1])
        else:
            raise ValueError("Incorrect mask")

    def __str__(self):
        return f'IP address {self.ip}'

    def __repr__(self):
        return f"IP address('{self.ip}')"

#testing
if __name__ == "__main__":
    ip1 = IPAddress('10.1.1.1/24')
    print(str(ip1), end = '\n\n')

    ip_list = []
    ip_list.append(ip1)
    print(ip_list)