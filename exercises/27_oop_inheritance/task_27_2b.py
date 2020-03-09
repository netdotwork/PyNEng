# -*- coding: utf-8 -*-

"""
Задание 27.2b

Дополнить класс MyNetmiko из задания 27.2a.

Переписать метод send_config_set netmiko, добавив в него проверку на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает вывод команд.

In [2]: from task_27_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""
from netmiko.cisco.cisco_ios import CiscoIosBase
from netmiko import ConnectHandler
#import netmiko


class ErrorInCommand(Exception):
    pass


class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()
        self._device_params = device_params

    def _check_error_in_command(self, command, command_output):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        if any(error in command_output for error in errors):
            if errors[0] in command_output:
                raise ErrorInCommand(f"При выполнении команды \"{command}\" на устройстве {self._device_params['ip']} возникла ошибка \"Invalid input detected at '^' marker.\"")
            elif errors[1] in command_output:
                raise ErrorInCommand(f"При выполнении команды \"{command}\" на устройстве {self._device_params['ip']} возникла ошибка \"{''.join(errors[1])}\"")
            elif errors[2] in command_output:
                raise ErrorInCommand(f"При выполнении команды \"{command}\" на устройстве {self._device_params['ip']} возникла ошибка \"{''.join(errors[2])}\"")

    def send_command(self, command_string):
        result = super().send_command(command_string)
        self._check_error_in_command(command_string, result)
        return result

    def send_config_set(self, config_commands):
        result = super().send_config_set(config_commands)
        self._check_error_in_command(config_commands, result)
        return result

        #if config_commands:
        #    if isinstance(config_commands, str):
        #        result = super().send_config_set(config_commands)
        #        self._check_error_in_command(config_commands, result)
        #        return result
        #    elif isinstance(config_commands, list):
        #        result = super().send_config_set(config_commands[0])
        #        self._check_error_in_command(config_commands[0], result)
        #        if len(config_commands) > 1:
        #            for c in config_commands[1:]:
        #                result += super().send_config_set(c)
        #                self._check_error_in_command(c, result)
        #            return result
        #        else:
        #            return result

#testing
if __name__ == "__main__":
    device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.2",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

    r1 = MyNetmiko(**device_params)

    print(r1.send_config_set('do sh ip int br'))

    print(r1.send_config_set('sh ip int br'))

    print(r1.send_config_set('lo'))