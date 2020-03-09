# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

"""

import yaml
import netmiko


def send_show_command(device, command):
    print(f"connection to device {device['ip']}")
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        return result


#testing
if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        templates = yaml.safe_load(f)
        print(send_show_command(templates[0], command))
# for all devices from yaml
        for dev in templates:
            print(send_show_command(dev, command))