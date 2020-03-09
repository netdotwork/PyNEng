# -*- coding: utf-8 -*-
'''
Задание 18.6

Для заданий 18 раздела нет тестов!

В этом задании выложен файл parse_dhcp_snooping.py.
В файле parse_dhcp_snooping.py нельзя ничего менять.

В файле созданы несколько функций и описаны аргументы командной строки,
которые принимает файл.

Есть поддержка аргументов для выполнения всех действий, которые,
в предыдущих заданиях, выполнялись в файлах create_db.py, add_data.py и get_data.py.

В файле parse_dhcp_snooping.py есть такая строка:
import parse_dhcp_snooping_functions as pds

И задача этого задания в том, чтобы создать все необходимые функции,
в файле parse_dhcp_snooping_functions.py на основе информации в файле parse_dhcp_snooping.py.

Из файла parse_dhcp_snooping.py, необходимо определить:
* какие функции должны быть в файле parse_dhcp_snooping_functions.py
* какие параметры создать в этих функциях

Необходимо создать соответствующие функции и перенести в них функционал,
который описан в предыдущих заданиях.

Вся необходимая информация, присутствует в функциях create, add, get,
в файле parse_dhcp_snooping.py.

В принципе, для выполнения задания, не обязательно разбираться с модулем argparse.
Но, вы можете почитать о нем в разделе https://natenka.gitbook.io/pyneng/part_ii/12_useful_modules/argparse.

Для того, чтобы было проще начать, попробуйте создать необходимые функции в файле
parse_dhcp_snooping_functions.py и просто выведите аргументы функций, используя print.

Потом, можно создать функции, которые запрашивают информацию из БД
(базу данных можно скопировать из предыдущих заданий).

Можно создавать любые вспомогательные функции в файле parse_dhcp_snooping_functions.py,
а не только те, которые вызываются из файла parse_dhcp_snooping.py.


Проверьте все операции:
* создание БД
* добавление информации о коммутаторах
* добавление информации на основании вывода sh ip dhcp snooping binding из файлов
* выборку информации из БД (по параметру и всю информацию)

Чтобы было проще понять, как будет выглядеть вызов скрипта,
ниже несколько примеров.
В примерах показывается вариант, когда в базе данных есть поля active и last_active,
но можно также использовать вариант без этих полей.

$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          имя БД
  -k {mac,ip,vlan,interface,switch}
                        параметр для поиска записей
  -v VALUE              значение параметра
  -a                    показать все содержимое БД


$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      файл(ы), которые надо добавить

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  имя БД
  -s            если флаг установлен, добавлять данные коммутаторов, иначе -
                DHCP записи


$ python parse_dhcp_snooping.py create_db
Создаю БД dhcp_snooping.db со схемой dhcp_snooping_schema.sql
Создаю базу данных...


$ python parse_dhcp_snooping.py add sw[1-3]_dhcp_snooping.txt
Читаю информацию из файлов
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Добавляю данные по DHCP записях в dhcp_snooping.db


$ python parse_dhcp_snooping.py add -s switches.yml
Добавляю данные о коммутаторах

$ python parse_dhcp_snooping.py get
В таблице dhcp такие записи:

Активные записи:

-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2019-03-08 16:47:52
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2019-03-08 16:47:52
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2019-03-08 16:47:52
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2019-03-08 16:47:52
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2019-03-08 16:47:52
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2019-03-08 16:47:52
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2019-03-08 16:47:52
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2019-03-08 16:47:52
-----------------  ---------------  --  ----------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vlan -v 10
Данные из БД: dhcp_snooping.db
Информация об устройствах с такими параметрами: vlan 10

Активные записи:

-----------------  ----------  --  ---------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1  2019-03-08 16:47:52
-----------------  ----------  --  ---------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')

'''
import sys
import sqlite3
import os
import yaml
import re
from tabulate import tabulate
from datetime import datetime, timedelta


def create_db(db_name, schema_filename):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("Создаю базу данных...")
        con = sqlite3.connect(db_name)
        with open(schema_filename) as f:
            con.executescript(f.read())
    else:
        print("База данных существует")


def add_data_switches(db_filename, yaml_files):
    for yaml_file in yaml_files:
        with open(yaml_file) as f:
            yml_template = yaml.safe_load(f)
            switches_list = [(key, value) for key, value in yml_template['switches'].items()]

            db_exists = os.path.exists(db_filename)
            if not db_exists:
                print('База данных не существует. Перед добавлением данных, ее надо создать')
                break
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
                        #pass
                        print(f'При добавлении данных: {row} Возникла ошибка: UNIQUE constraint failed: switches.hostname')

def add_data(db_filename, dhcp_list):
    result = []
    regex = r'((?:\w+:){5}\w+)\s+(\S+)\s+\S+\s+\S+\s+(\d+){1,4}\s+(\S+)'
    for l in dhcp_list:
        with open(l) as ff:
            for r in re.finditer(regex, ff.read()):
                rr = list(r.groups())
                rr.append(re.sub(r'new_data/|_dhcp_snooping.txt', '', l))
                result.append(tuple(rr))

# для неактивных записей меняем только поле active на 0, а поле last_active оставляем без изменений
    db_exists = os.path.exists(db_filename)
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
    else:
        con = sqlite3.connect(db_filename)
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

def get_data(db_filename, key, value):

    con = sqlite3.connect(db_filename)
    cursor = con.cursor()

    query_dict = {
        'mac': 'select * from dhcp where mac = ? and active = ?',
        'ip': 'select * from dhcp where ip = ? and active = ?',
        'vlan': 'select * from dhcp where vlan = ? and active = ?',
        'interface': 'select * from dhcp where interface = ? and active = ?',
        'switch': 'select * from dhcp where switch = ? and active = ?'
    }

    keys = query_dict.keys()
    query = query_dict[key]
    cursor.execute(query, (value, 1))
    db_list = cursor.fetchall()
    if len(db_list) >= 1:
#        print(f'Информация об устройствах с такими параметрами: {key} {value}')
        print('')
        print('Активные записи:', end='\n\n')
        print(tabulate(db_list))

    cursor.execute(query, (value, 0))
    db_list = cursor.fetchall()
    if len(db_list) >= 1:
#        print(f'Информация об устройствах с такими параметрами: {key} {value}')
        print('')
        print('Неактивные записи:', end='\n\n')
        print(tabulate(db_list))


def get_all_data(db_filename):

    con = sqlite3.connect(db_filename)
    cursor = con.cursor()
    cursor.execute('select * from dhcp where active = 1')

    print('')
    print('Активные записи:', end = '\n\n')
    print(tabulate(cursor.fetchall()))