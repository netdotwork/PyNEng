# -*- coding: utf-8 -*-
"""
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""

import textfsm
import clitable
#from textfsm import clitable
import netmiko
import yaml
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed
from task_22_4 import send_and_parse_show_command
from tabulate import tabulate
import logging
from datetime import datetime
import time


def send_and_parse_command_parallel(devices, command, filename, templates_path='templates', limit=3):
    '''
    Функция-генератор html-таблицы. Отправляет на каждое устройство из файла .yaml команду command,
    одновременно подключаясь к нескольким устройствам (по умолчанию, limit=3).
    Используя TextFSM-шаблоны (директория temlates, по умолчанию) и index-файл обрабатывает вывод
    с каждого устройства и записывает в файл (filename) в виде html-таблицы.
    Действия логируются с помощью модуля logging.
    devices - список словарей с параметрами устройств в yaml-формате. Обязательно наличие ключа device_type
    command - команда show, которую требуется выполнить на каждом устройстве
    filename - файл, куда сохраняется вывод с каждого устройства в виде таблицы
    limit - число потоков
    templates_path - директория с TextFSM-шаблонами и index-файлом
    '''
    logging_result = {}
    logging.basicConfig(
        format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
        level=logging.INFO)
    with open(devices) as f:
        templates = yaml.safe_load(f)
    with ThreadPoolExecutor(max_workers = limit) as executor:
        future_list = []
        for device in templates:
            logging.info(f"{datetime.now().time()} Connection to {device['ip']}")
            future = executor.submit(send_and_parse_show_command, device, command, templates_path)
            future_list.append(future)
        with open(filename, 'w') as ff:
            for fff in as_completed(future_list):
                logging.info(f"Future done {fff}")
                #print(tabulate(ff.result(), headers='keys'))
                #with open(filename, 'w') as fff:
                ff.write(tabulate(fff.result(), headers='keys', tablefmt='html'))
            logging.info(f"Check result in {filename}")


#testing
if __name__ == "__main__":
    send_and_parse_command_parallel('devices.yaml', 'sh ip int br', 'task_22_5_output.html')