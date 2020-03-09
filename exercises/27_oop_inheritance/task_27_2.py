# -*- coding: utf-8 -*-

"""
Задание 27.2

Создать класс MyNetmiko, который наследует класс CiscoIosBase из netmiko.

Переписать метод __init__ в классе MyNetmiko таким образом, чтобы после подключения по SSH выполнялся переход в режим enable.

Для этого в методе __init__ должен сначала вызываться метод __init__ класса CiscoIosBase, а затем выполнялся переход в режим enable.

Проверить, что в классе MyNetmiko доступны методы send_command и send_config_set

In [2]: from task_27_2 import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from netmiko.cisco.cisco_ios import CiscoIosBase
from netmiko import ConnectHandler
#import netmiko


class MyNetmiko(CiscoIosBase):
    '''
    создаем дочерний класс, MyNetmiko. В качестве родительского класса для MyNetmiko используем класс CiscoIosBase, который
    находится в модуле netmiko, в директории cisco, в модуле cisco_ios.py.
    Дальше напишем свой метод __init__, который наследует __init__ из класса CiscoIosBase (с помощью super()), который в свою очередь,
    наследует __init__ от родительского класса CiscoBaseConnection, который наследует __init__ от родительского класса BaseConnection (здесь метод __init__
    требует распакованный словарь с аргументами).
    В классе BaseConnection есть метод enable, который мы уже наследовали, но там же, в описании метода
    https://github.com/ktbyers/netmiko/blob/98c3825a1ebbb3c9441b9b12a2e3b67c5107dcb2/netmiko/base_connection.py#L35
    указано, что для подключения используется метод ConnectHandler, которого нет ни в одном из классов, которые мы ранее наследовали.
    Метод ConnectHandler возвращает переменную ConnectionClass, равную device_type (в нашем случае, cisco_ios),
    которая нужна для подключения в __init__, в родительском классе BaseConnection
    '''
    def __init__(self, **device_params):
        super().__init__(**device_params)
        # ----- ошибка - родительский метод __init__ уже выполняет подключение. Достаточно будет только перейти в enable
        #with ConnectHandler(**device_params) as self._ssh:
            #self._ssh.enable()
        self.enable()

#testing
if __name__ == "__main__":
    device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

    r1 = MyNetmiko(**device_params)

    print(r1.send_command('sh ip int br'))