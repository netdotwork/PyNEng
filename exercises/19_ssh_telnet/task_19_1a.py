# -*- coding: utf-8 -*-
"""
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
"""

import yaml
import netmiko


def send_show_command(device, command):
    try:
        print(f"connection to device {device['ip']}")
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except (netmiko.ssh_exception.NetMikoAuthenticationException):
        print("Authentication failure: unable to connect")


#testing
if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        templates = yaml.safe_load(f)
        print(send_show_command(templates[0], command))
# for all devices from yaml
        for dev in templates:
            print(send_show_command(dev, command))