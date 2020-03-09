# -*- coding: utf-8 -*-
"""
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""

import textfsm
import clitable
#from textfsm import clitable
import netmiko
import yaml


def send_and_parse_show_command(device_dict, command, templates_path, index='index'):
    attributes_dict = {'Command': command, 'Vendor': device_dict['device_type']}
    with netmiko.ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        sh_command_result = ssh.send_config_set(command)
        #return type(sh_command_result)
        cli_table = clitable.CliTable(index, templates_path)
        cli_table.ParseCmd(sh_command_result, attributes_dict)
        header = list(cli_table.header)
        data_rows = [list(row) for row in cli_table]
        output_list = [dict(zip(header, r)) for r in data_rows]
        return output_list

#testing
if __name__ == "__main__":
    command1 = "sh ip int br"
    with open('devices.yaml') as ff:
        templates = yaml.safe_load(ff)
        for template in templates:
            print(send_and_parse_show_command(template, command1, templates_path='templates'))