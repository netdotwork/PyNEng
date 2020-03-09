# -*- coding: utf-8 -*-

"""
Задание 25.2

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
* _write_line - принимает как аргумент строку и отправляет на оборудование строку преобразованную в байты и добавляет перевод строки в конце.
  Метод _write_line должен использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод полученный с обрудования

Пример создания экземпляра класса:
In [2]: from task_25_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command('sh ip int br')
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

"""
import telnetlib
import time


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

    def send_show_command(self, sh_command):
        self.tt.write(sh_command.encode('ascii') + b'\n')

        #time.sleep(1)

        #for all commands (in all methods)
        #output = self.tt.read_very_eager().decode('ascii')

        #for single show command in this method
        self.tt.read_until(b'#', timeout = 2)
        output = self.tt.read_until(b'#', timeout = 1)
        return output.decode('ascii')

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
    print(r1.send_show_command('sh ip int br'))
    #т.к. соединение закрыто, открываем его снова, для второго теста
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_show_command('sh ver'))