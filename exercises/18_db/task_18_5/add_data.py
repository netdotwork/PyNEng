# -*- coding: utf-8 -*-
'''
Задание 18.5

Для заданий 18 раздела нет тестов!

После выполнения заданий 18.1 - 18.5 в БД остается информация о неактивных записях.
И, если какой-то MAC-адрес не появлялся в новых записях, запись с ним,
может остаться в БД навсегда.

И, хотя это может быть полезно, чтобы посмотреть, где MAC-адрес находился в последний раз,
постоянно хранить эту информацию не очень полезно.

Например, если запись в БД уже больше месяца, то её можно удалить.

Для того, чтобы сделать такой критерий, нужно ввести новое поле,
в которое будет записываться последнее время добавления записи.

Новое поле называется last_active и в нем должна находиться строка,
в формате: YYYY-MM-DD HH:MM:SS.

В этом задании необходимо:
* изменить, соответственно, таблицу dhcp и добавить новое поле.
 * таблицу можно поменять из cli sqlite, но файл dhcp_snooping_schema.sql тоже необходимо изменить
* изменить скрипт add_data.py, чтобы он добавлял к каждой записи время

Получить строку со временем и датой, в указанном формате, можно с помощью функции datetime в запросе SQL.
Синтаксис использования такой:
sqlite> insert into dhcp (mac, ip, vlan, interface, switch, active, last_active)
   ...> values ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1', '0', datetime('now'));

То есть вместо значения, которое записывается в базу данных, надо указать datetime('now').

После этой команды в базе данных появится такая запись:
mac                ip               vlan        interface        switch      active      last_active
-----------------  ---------------  ----------  ---------------  ----------  ----------  -------------------
00:09:BC:3F:A6:50  192.168.100.100  1           FastEthernet0/7  sw1         0           2019-03-08 11:26:56
'''
import os
import sqlite3
import yaml
import re
from datetime import datetime


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
#                rr.append(l[-21:l.find('dhcp')].replace('_', ''))
                rr.append(re.sub(r'new_data/|_dhcp_snooping.txt', '', l))
                result.append(tuple(rr))

# для неактивных записей меняем только поле active на 0, а поле last_active оставляем без изменений
    db_exists = os.path.exists(db_filename)
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
    else:
        con = sqlite3.connect(db_filename)
        print('Добавляю данные в таблицу dhcp...')
        replace_dhcp_active = "update dhcp set active = ? where mac = ?"
        with con:
            for c in con.execute('select * from dhcp'):
                con.execute(replace_dhcp_active, (0, c[0]))

# для активных записей меняем active на 1 и указываем дату внесения изменений - в поле last_active
        for row in result:
            try:
                with con:
                    query_dhcp = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active, last_active)
                                    values (?, ?, ?, ?, ?, 1, datetime('now'))'''
                    con.execute(query_dhcp, row)
            except sqlite3.IntegrityError as err:
                print(f'При добавлении данных: {row} Возникла ошибка: UNIQUE constraint failed: dhcp.mac')
        con.close()


if __name__ == '__main__':
    # создаем бд, если её нет
    db = 'dhcp_snooping.db'
    schema = 'dhcp_snooping_schema.sql'
    db_create(db, schema)
    # сперва используем вывод из этого списка, а только затем из следующего
    #dhcp_sn = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    dhcp_sn = ['new_data/sw1_dhcp_snooping.txt', 'new_data/sw2_dhcp_snooping.txt', 'new_data/sw3_dhcp_snooping.txt']
    file = 'switches.yml'
    add_data_to_switches(file, db)
    add_data_to_dhcp(dhcp_sn, db)