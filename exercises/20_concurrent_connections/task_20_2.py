# -*- coding: utf-8 -*-
"""
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
import netmiko
from concurrent.futures import ThreadPoolExecutor
import yaml
from itertools import repeat
import re


def send_show_command(device, command):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(command)
        return result

def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers = limit) as executor:
        result = executor.map(send_show_command, devices, repeat('sh ip int br'))
    with open(filename, 'w') as f:
        for r in result:
            for line in r.split('\n'):
                match = re.search(r'config (\S+)|.*CNTL\/Z|.*end|(\w+)#', line)
                if match:
                    continue
                else:
                    print(line)
                    f.write(line +'\n')


#testing
if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as ff:
        templates = yaml.safe_load(ff)
        send_show_command_to_devices(templates, command, 'task_20_2_output.txt')