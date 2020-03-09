# -*- coding: utf-8 -*-
'''
Задание 18.5a

Для заданий 18 раздела нет тестов!

После выполнения задания 18.5, в таблице dhcp есть новое поле last_active.

Обновите скрипт add_data.py, таким образом, чтобы он удалял все записи,
которые были активными более 7 дней назад.

Для того, чтобы получить такие записи, можно просто вручную обновить поле last_active в некоторых записях и поставить время 7 или более дней.

В файле задания описан пример работы с объектами модуля datetime.
Показано как получить дату 7 дней назад. С этой датой надо будет сравнивать время last_active.

Обратите внимание, что строки с датой, которые пишутся в БД, можно сравнивать между собой.

'''

from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=7)

#print(now)
#print(week_ago)
#print(now > week_ago)
#print(str(now) > str(week_ago))

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

        delete_dhcp_week_ago = "delete from dhcp where mac = ?"

        now = datetime.today().replace(microsecond=0)
        week_ago = now - timedelta(days=7)

        with con:
            for c in con.execute('select * from dhcp'):
                if c[6] < str(week_ago):
                    con.execute(delete_dhcp_week_ago, (c[0], ))
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
    # создаем бд, есть её нет
    db = 'dhcp_snooping.db'
    schema = 'dhcp_snooping_schema.sql'
    db_create(db, schema)
    # сперва используем вывод из этого списка, а только затем из следующего
    #dhcp_sn = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    dhcp_sn = ['new_data/sw1_dhcp_snooping.txt', 'new_data/sw2_dhcp_snooping.txt', 'new_data/sw3_dhcp_snooping.txt']
    file = 'switches.yml'
    add_data_to_switches(file, db)
    add_data_to_dhcp(dhcp_sn, db)