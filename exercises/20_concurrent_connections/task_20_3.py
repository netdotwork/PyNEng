# -*- coding: utf-8 -*-
"""
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

import netmiko
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml
import re


def send_command(device, command):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(strip_prompt=False, command_string=command, strip_command=False)
        return result


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers = limit) as executor:
        result1 = executor.map(send_command, devices, [command for command in commands_dict.values()])
    with open(filename, 'w') as f:
        for r in result1:
            match = re.search(r'(.*)\n(\w+)#', r, re.DOTALL)
            f.write(f'{match.group(2)}#{match.group(1)}\n')


#testing
if __name__ == "__main__":
    commands = {
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "show arp",
    "192.168.100.3": "show ip int br",
    }
    with open('devices.yaml') as ff:
        templates = yaml.safe_load(ff)
        send_command_to_devices(templates, commands, 'task_20_3_output.txt')