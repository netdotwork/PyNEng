# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""
import csv
import re


def write_dhcp_snooping_to_csv(files, out):
    regex = re.compile(r'(\S+)\s+((?:\d+.){3}\d+)\s+\S+\s+\S+\s+(\S+)\s+(\S+)')
    headers = [['switch', 'mac', 'ip', 'vlan', 'interface']]
    csv_list = []
    for file in files:
        with open(file, encoding = 'UTF-8') as f:
            for value in regex.finditer(f.read()):
                reg_list = [file[0:file.find('_')], value.group(1), value.group(2), value.group(3), value.group(4)]
                csv_list.append(reg_list)
    headers.extend(csv_list)
    with open(out, 'w', encoding = 'UTF-8') as ff:
        writer = csv.writer(ff)
        writer.writerows(headers)

#testing
if __name__ == '__main__':
    filenames = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    output = 'output.csv'
    write_dhcp_snooping_to_csv(filenames, output)