# -*- coding: utf-8 -*-
"""
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
"""

import yaml
import netmiko


def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"connection to device {device['ip']}")
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
        return result


#testing
if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    with open('devices.yaml') as f:
        templates = yaml.safe_load(f)
        print(send_config_commands(templates[0], commands, log=False))
# for all devices from yaml
        for dev in templates:
            print(send_config_commands(dev, commands))