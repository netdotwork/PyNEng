# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#!/home/user/virtenvs/pyneng-py3-1/bin/python3
ip = input("Enter your ip address with mask, please: ")
ip1 = ip.split('/')
ip2 = ip1[0].split('.')

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(ip2[0]), int(ip2[1]), int(ip2[2]), int(ip2[3])))

mask = ip[ip.find('/')::]
#print(mask)
mask1 = int(mask.strip('/'))

mask2 = '1' * mask1 + '0' * (32-mask1)
#print(mask2)

mask4 = int(mask2[0:8], 2)
#print(mask4)

mask_template = '''
Mask:
{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:<08b} {2:<08b} {3:<08b} {4:<08b}
'''
print(mask_template.format(mask, int(mask2[0:8], 2), int(mask2[8:16], 2), int(mask2[16:24], 2), int(mask2[24::], 2)))