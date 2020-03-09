# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)


def parse_sh_version(sh_version):
    regex = (r'Cisco.*Software.+Software.+, Version (\d+.+), RELEASE.*Version.*uptime is (\d+\s+\S+,\s+\d+\s+\S+,\s+\d+\s+\S+).*image file is \"(\S+)\"')
    t = re.findall(regex, sh_version, re.DOTALL)
    t1 = (t[0][0], t[0][2], t[0][1])
    return t1

def write_inventory_to_csv(data_filenames, csv_filename):
    headers = ["hostname", "ios", "image", "uptime"]
    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
    for ff in data_filenames:
        with open(ff, encoding = 'UTF-8') as fff:
            value_tuple = parse_sh_version(fff.read())
            value_list = [ff[11:ff.find('.')], value_tuple[0], value_tuple[1], value_tuple[2]]
            with open(csv_filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(value_list)


#testing
if __name__ == '__main__':
    filenames_list = ['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt']
    write_inventory_to_csv(filenames_list, 'task_17_2_output.csv')