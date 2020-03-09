# -*- coding: utf-8 -*-

"""
Задание 27.2d

Дополнить класс MyNetmiko из задания 27.2c или задания 27.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен работать точно так же как метод send_config_set в netmiko.

Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_27_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

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

    def send_command(self, *args, **kwargs):
        result = super().send_command(*args, **kwargs)
        self._check_error_in_command(args[0], result)
        return result

    def send_config_set(self, config_commands, ignore_errors=True):
        result = super().send_config_set(config_commands)
        if ignore_errors:
            return super().send_config_set(config_commands)
        else:
            self._check_error_in_command(config_commands, result)
            return result


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

    print(r1.send_config_set('lo'))

    print(r1.send_config_set('lo', ignore_errors=True))

    print(r1.send_config_set('lo', ignore_errors=False))