# -*- coding: utf-8 -*-
'''
Задание 18.3

Для заданий 18 раздела нет тестов!

В прошлых заданиях информация добавлялась в пустую БД.
В этом задании, разбирается ситуация, когда в БД уже есть информация.

Скопируйте скрипт add_data.py из задания 18.1 и попробуйте выполнить его повторно, на существующей БД.
Должен быть такой вывод:
$ python add_data.py
Добавляю данные в таблицу switches...
При добавлении данных: ('sw1', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw2', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw3', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
Добавляю данные в таблицу dhcp...
При добавлении данных: ('00:09:BB:3D:D6:58', '10.1.10.2', '10', 'FastEthernet0/1', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:04:A3:3E:5B:69', '10.1.5.2', '5', 'FastEthernet0/10', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:05:B3:7E:9B:60', '10.1.5.4', '5', 'FastEthernet0/9', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:07:BC:3F:A6:50', '10.1.10.6', '10', 'FastEthernet0/3', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
... (вывод сокращен)

При создании схемы БД, было явно указано, что поле MAC-адрес, должно быть уникальным.
Поэтому, при добавлении записи с таким же MAC-адресом, возникает исключение (ошибка).
В задании 18.1 исключение обрабатывается и выводится сообщение на стандартный поток вывода.

В этом задании считается, что информация периодически считывается с коммутаторов и записывается в файлы.
После этого, информацию из файлов надо перенести в базу данных.
При этом, в новых данных могут быть изменения: MAC пропал, MAC перешел на другой порт/vlan, появился новый MAC и тп.

В этом задании в таблице dhcp надо создать новое поле active, которое будет указывать является ли запись актуальной.
Новая схема БД находится в файле dhcp_snooping_schema.sql

Поле active должно принимать такие значения:
* 0 - означает False. Используется для того, чтобы отметить запись как неактивную
* 1 - True. Используется чтобы указать, что запись активна

Каждый раз, когда информация из файлов с выводом DHCP snooping добавляется заново,
надо пометить все существующие записи (для данного коммутатора), как неактивные (active = 0).
Затем можно обновлять информацию и пометить новые записи, как активные (active = 1).

Таким образом, в БД останутся и старые записи, для MAC-адресов, которые сейчас не активны,
и появится обновленная информация для активных адресов.

Например, в таблице dhcp такие записи:
mac                ip          vlan        interface         switch      active
-----------------  ----------  ----------  ----------------  ----------  ----------
00:09:BB:3D:D6:58  10.1.10.2   10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.5.2    5           FastEthernet0/10  sw1         1
00:05:B3:7E:9B:60  10.1.5.4    5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6   10          FastEthernet0/3   sw1         1
00:09:BC:3F:A6:50  192.168.10  1           FastEthernet0/7   sw1         1


И надо добавить такую информацию из файла:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.15.2        63951       dhcp-snooping   15    FastEthernet0/15
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/5


После добавления данных таблица должна выглядеть так:
mac                ip               vlan        interface         switch      active
-----------------  ---------------  ----------  ---------------   ----------  ----------
00:09:BC:3F:A6:50  192.168.100.100  1           FastEthernet0/7   sw1         0
00:09:BB:3D:D6:58  10.1.10.2        10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.15.2        15          FastEthernet0/15  sw1         1
00:05:B3:7E:9B:60  10.1.5.4         5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6        10          FastEthernet0/5   sw1         1

Новая информация должна перезаписывать предыдущую:
* MAC 00:04:A3:3E:5B:69 перешел на другой порт и попал в другой интерфейс и получил другой адрес
* MAC 00:07:BC:3F:A6:50 перешел на другой порт

Если какого-то MAC-адреса нет в новом файле, его надо оставить в бд со значением active = 0:
* MAC-адреса 00:09:BC:3F:A6:50 нет в новой информации (выключили комп)


Измените скрипт add_data.py таким образом, чтобы выполнялись новые условия и заполнялось поле active.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

> Для проверки корректности запроса SQL, можно выполнить его в командной строке, с помощью утилиты sqlite3.

Для проверки задания и работы нового поля, сначала добавьте в бд информацию из файлов sw*_dhcp_snooping.txt,
а потом добавьте информацию из файлов new_data/sw*_dhcp_snooping.txt

Данные должны выглядеть так (порядок строк может быть любым)
-----------------  ---------------  --  ----------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  0
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  0
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2        15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65       20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77       10  FastEthernet0/4   sw2  1
-----------------  ---------------  --  ----------------  ---  -


'''
import os
import sqlite3
import yaml
import re


def db_create(db_name, schema_filename):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("Создаю базу данных...")
        con = sqlite3.connect(db_name)
        with open(schema_filename) as f:
            con.executescript(f.read())
    else:
        print("База данных существует")


def add_data_to_switches(yaml_file, db_filename):
    with open(yaml_file) as f:
        yml_template = yaml.safe_load(f)
    switches_list = [(key, value) for key, value in yml_template['switches'].items()]

    db_exists = os.path.exists(db_filename)
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
    else:
        con = sqlite3.connect(db_filename)
        print('Добавляю данные в таблицу switches...')
        for row in switches_list:
            try:
                with con:
                    query_switches = '''insert into switches (hostname, location)
                                        values (?, ?)'''
                    con.execute(query_switches, row)
            except sqlite3.IntegrityError as err:
                pass
                #print(f'При добавлении данных: {row} Возникла ошибка: UNIQUE constraint failed: switches.hostname')

def add_data_to_dhcp(dhcp_list, db_filename):
    result = []
    regex = r'((?:\w+:){5}\w+)\s+(\S+)\s+\S+\s+\S+\s+(\d+){1,4}\s+(\S+)'
    for l in dhcp_list:
        with open(l) as ff:
            for r in re.finditer(regex, ff.read()):
                rr = list(r.groups())
                rr.append(l[0:l.find('_')])
                result.append(tuple(rr))

    db_exists = os.path.exists(db_filename)
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
    else:
        con = sqlite3.connect(db_filename)
        cursor = con.cursor()
        print('Добавляю данные в таблицу dhcp...')
        replace_dhcp_active = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active)
                                 values (?, ?, ?, ?, ?, ?)'''
        cursor.execute('select * from dhcp')
        r1 = []
        for row in cursor.fetchall():
            r2 = list(row)
            r2[-1] = 0
            r1.append(tuple(r2))
        with con:
            con.executemany(replace_dhcp_active, r1)
# ошибка, которая приведет к бесконечному циклу:
#        with con:
#            for row in con.execute('select * from dhcp'):
#                r1 = list(row)
#                r1[-1] = 0
#                con.execute(replace_dhcp_active, tuple(r1))
        for row1 in result:
            try:
                with con:
                    query_dhcp = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active)
                                    values (?, ?, ?, ?, ?, 1)'''
                    con.execute(query_dhcp, row1)
            except sqlite3.IntegrityError as err:
                print(f'При добавлении данных: {row} Возникла ошибка: UNIQUE constraint failed: dhcp.mac')
        con.close()


if __name__ == '__main__':
    db = 'dhcp_snooping.db'
    schema = 'dhcp_snooping_schema.sql'
    db_create(db, schema)
    # сперва используем вывод из этого списка, а только затем из следующего
    #dhcp_sn = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    dhcp_sn = ['new_data/sw1_dhcp_snooping.txt', 'new_data/sw2_dhcp_snooping.txt', 'new_data/sw3_dhcp_snooping.txt']
    file = 'switches.yml'
    add_data_to_switches(file, db)
    add_data_to_dhcp(dhcp_sn, db)