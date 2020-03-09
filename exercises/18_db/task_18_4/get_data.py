# -*- coding: utf-8 -*-
'''
Задание 18.4

Для заданий 18 раздела нет тестов!

Скопировать файл get_data из задания 18.2.
Добавить в скрипт поддержку столбца active, который мы добавили в задании 18.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные. Если неактивных записей нет, не отображать заголовок "Неактивные записи".

Примеры выполнения итогового скрипта
$ python get_data.py
В таблице dhcp такие записи:

Активные записи:

-----------------  ----------  --  ----------------  ---  -
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2   15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4     5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6    3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7    3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20    5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65  20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4   sw2  1
-----------------  ----------  --  ----------------  ---  -

Неактивные записи:

-----------------  ---------------  -  ---------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100  1  FastEthernet0/7  sw1  0
00:C5:B3:7E:9B:60  10.1.5.40        5  FastEthernet0/9  sw2  0
-----------------  ---------------  -  ---------------  ---  -

$ python get_data.py vlan 5

Информация об устройствах с такими параметрами: vlan 5

Активные записи:

-----------------  ---------  -  ---------------  ---  -
00:05:B3:7E:9B:60  10.1.5.4   5  FastEthernet0/9  sw1  1
00:B4:A3:3E:5B:69  10.1.5.20  5  FastEthernet0/5  sw2  1
-----------------  ---------  -  ---------------  ---  -

Неактивные записи:

-----------------  ---------  -  ---------------  ---  -
00:C5:B3:7E:9B:60  10.1.5.40  5  FastEthernet0/9  sw2  0
-----------------  ---------  -  ---------------  ---  -


$ python get_data.py vlan 10

Информация об устройствах с такими параметрами: vlan 10

Активные записи:

-----------------  ----------  --  ---------------  ---  -
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5  sw1  1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1
00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4  sw2  1
-----------------  ----------  --  ---------------  ---  -
'''
import sys
import sqlite3
from tabulate import tabulate

def get_data():

    db_name = 'dhcp_snooping.db'

    con = sqlite3.connect(db_name)
    cursor = con.cursor()

    query_dict = {
        'mac': 'select * from dhcp where mac = ? and active = ?',
        'ip': 'select * from dhcp where ip = ? and active = ?',
        'vlan': 'select * from dhcp where vlan = ? and active = ?',
        'interface': 'select * from dhcp where interface = ? and active = ?',
        'switch': 'select * from dhcp where switch = ? and active = ?'
    }
    if len(sys.argv) >3 or len(sys.argv) == 2:
        print('Пожалуйста, введите два или ноль аргументов')
    elif sys.argv[1:]:
        key, value = sys.argv[1:]
        keys = query_dict.keys()
        if key in keys:
            query = query_dict[key]
            cursor.execute(query, (value, 1))
            db_list = cursor.fetchall()
            if len(db_list) >= 1:
                print(f'Информация об устройствах с такими параметрами: {key} {value}')
                print('Активные записи:')
                print(tabulate(db_list))

            cursor.execute(query, (value, 0))
            db_list = cursor.fetchall()
            if len(db_list) >= 1:
                print(f'Информация об устройствах с такими параметрами: {key} {value}')
                print('Неактивные записи:')
                print(tabulate(db_list))
        else:
            print('''Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch''')
    else:
        cursor.execute('select * from dhcp')
        print(tabulate(cursor.fetchall()))

if __name__ == '__main__':
    get_data()