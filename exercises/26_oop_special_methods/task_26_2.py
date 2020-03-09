# -*- coding: utf-8 -*-

"""
Задание 26.2

Добавить к классу CiscoTelnet из задания 25.2x поддержку работы в менеджере контекста.
При выходе из блока менеджера контекста должно закрываться соединение.
Все исключения, которые возникли в менеджере контекста, должны генерироваться после выхода из блока with.

Пример работы:

In [14]: r1_params = {
    ...:     'ip': '192.168.100.1',
    ...:     'username': 'cisco',
    ...:     'password': 'cisco',
    ...:     'secret': 'cisco'}

In [15]: from task_26_2 import CiscoTelnet

In [16]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:
sh clock
*19:17:20.244 UTC Sat Apr 6 2019
R1#

In [17]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:     raise ValueError('Возникла ошибка')
    ...:
sh clock
*19:17:38.828 UTC Sat Apr 6 2019
R1#
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-f3141be7c129> in <module>
      1 with CiscoTelnet(**r1_params) as r1:
      2     print(r1.send_show_command('sh clock'))
----> 3     raise ValueError('Возникла ошибка')
      4

ValueError: Возникла ошибка
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self.tt.close()

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

    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command('sh clock'))

    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command('sh clock'))
        raise ValueError('Возникла ошибка')