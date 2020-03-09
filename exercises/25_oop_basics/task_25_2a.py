# -*- coding: utf-8 -*-

"""
Задание 25.2a

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, полученные после обработки с помощью TextFSM.
При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами



Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_25_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command('sh ip int br', parse=False)
Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

In [5]: r1.send_show_command('sh ip int br', parse=True)
Out[5]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '190.16.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.100',
  'address': '10.100.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.200',
  'address': '10.200.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.300',
  'address': '10.30.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback0',
  'address': '10.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback55',
  'address': '5.5.5.5',
  'status': 'up',
  'protocol': 'up'}]
"""
import telnetlib
import textfsm
import time
import clitable
from pprint import pprint
#from textfsm import clitable

class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        t = telnetlib.Telnet(ip)
        self.tt = t
        print('Connection to device {}'.format(ip))
        t.read_until(b'Username:')
        t.write(username.encode('ascii') + b'\n')

        t.read_until(b'Password:')
        t.write(password.encode('ascii') + b'\n')
        t.write(b'enable\n')

        t.read_until(b'Password:')
        t.write(secret.encode('ascii') + b'\n')
        t.write(b'terminal length 0\n')

        #time.sleep(1)

        t.read_until(b'#', timeout = 2)

    def _write_line(self, line):
        self.tt.write(line.encode('ascii') + b'\n')

        #time.sleep(1)

        self.tt.read_until(b'#', timeout = 2)

    def send_show_command(self, sh_command, parse, templates='templates'):
        self.tt.write(sh_command.encode('ascii') + b'\n')

        #time.sleep(1)

        #for all commands (in all methods)
        #output = self.tt.read_very_eager().decode('ascii')

        #for single show command in this method
        self.tt.read_until(b'#', timeout = 2)
        command_output = self.tt.read_until(b'#', timeout = 1)

        attributes_dict = {'Command': sh_command}
        cli_table = clitable.CliTable('index', templates)
        cli_table.ParseCmd(command_output.decode('ascii'), attributes_dict)
        header = list(cli_table.header)
        data_rows = [list(row) for row in cli_table]
        output_list = [dict(zip(header, r)) for r in data_rows]

        if parse:
            return output_list
        else:
            return command_output.decode('ascii')


#testing
if __name__ == "__main__":
    r1_params = {
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}
    r1 = CiscoTelnet(**r1_params)
    r1._write_line('sh arp')
    #print(r1.send_show_command('sh ip int br'))
    print(r1.send_show_command('sh ip int br', parse=False))
    #т.к. соединение закрыто, открываем его снова, для второго теста
    r1 = CiscoTelnet(**r1_params)
    pprint(r1.send_show_command('sh ip int br', parse=True))