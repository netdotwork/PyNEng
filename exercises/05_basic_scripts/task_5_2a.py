# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

#!/home/user/virtenvs/pyneng-py3-1/bin/python3
# works for addresses like 192.168.1.1/24, but doesn't work for addresses like 10.1.1.0/24, because 10 = 0b1010, but we need to get 0b00001010
ip = input("Enter your ip address with mask, please: ")
ip1 = ip.split('/')
ip2 = ip1[0].split('.')
ip3 = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(ip2[0]), int(ip2[1]), int(ip2[2]), int(ip2[3]))
mask = '1' * int(ip1[1]) + '0' * (32-int(ip1[1]))
network = int(ip3, 2) & int(mask, 2)
network1 = bin(network)
network2 = str(network1)

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template.format(int(network2[2:10], 2), int(network2[10:18], 2), int(network2[18:26], 2), int(network2[26::], 2)))

mask1 = ip[ip.find('/')::]

mask_template = '''
Mask:
{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:<08b} {2:<08b} {3:<08b} {4:<08b}
'''
print(mask_template.format(mask1, int(mask[0:8], 2), int(mask[8:16], 2), int(mask[16:24], 2), int(mask[24::], 2)))