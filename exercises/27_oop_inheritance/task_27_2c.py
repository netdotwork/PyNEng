# -*- coding: utf-8 -*-

"""
Задание 27.2c

Проверить, что метод send_command класса MyNetmiko из задания 27.2b, принимает дополнительные аргументы (как в netmiko), кроме команды.

Если возникает ошибка, переделать метод таким образом, чтобы он принимал любые аргументы, которые поддерживает netmiko.


In [2]: from task_27_2c import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br', strip_command=False)
Out[4]: 'sh ip int br\nInterface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip int br', strip_command=True)
Out[5]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

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
# альтернативный вариант - указать все параметры родительского метода
#        self,
#        command_string,
#        expect_string=None,
#        delay_factor=1,
#        max_loops=500,
#        auto_find_prompt=True,
#        strip_prompt=True,
#        strip_command=True,
#        normalize=True,
#        use_textfsm=False,
#        textfsm_template=None,
#        use_genie=False,
#    ):
        result = super().send_command(*args, **kwargs)
# ультернативный вариант - использовать параметры дочернего метода в качестве аргументов для родительского
# но лучше использовать распаковку переменных с помощью *args (списки) и **kwargs (словари)
#        command_string=command_string,
#        expect_string=expect_string,
#        delay_factor=delay_factor,
#        max_loops=max_loops,
#        auto_find_prompt=True,
#        strip_prompt=True,
#        strip_command=True,
#        normalize=True,
#        use_textfsm=False,
#        textfsm_template=textfsm_template,
#        use_genie=False
#        )
        self._check_error_in_command(args[0], result)
        return result

    def send_config_set(self, config_commands):
        result = super().send_config_set(config_commands)
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

    print(r1.send_command('sh ip int br', strip_command=False, strip_prompt=False))

    print(r1.send_command('sh ip int br', strip_command=True))