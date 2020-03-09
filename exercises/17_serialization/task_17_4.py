# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (пример mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.

Для части пользователей запись только одна и тогда в итоговый файл надо записать только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_datetimestr_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.

Функцию convert_datetimestr_to_datetime использовать не обязательно.

"""

import datetime
import csv
from operator import itemgetter

def convert_datetimestr_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_file, output_file):

    email_list = []
    repeated_email_list = []

    f = open(source_file, encoding = 'UTF-8')
    ff = open(output_file, 'w', encoding = 'UTF-8')
    reader = csv.DictReader(f)
    for row in reader:
        email_list.append(row['Email'])
    sorted_email_list = sorted(email_list)
    for counter, value in enumerate(sorted_email_list):
        if counter == len(sorted_email_list)-1:
            break
        elif value == sorted_email_list[counter+1]:
            repeated_email_list.append(value)
    uniq_repeated_email_list = list(set(repeated_email_list))

    f.seek(0)
    reader = csv.reader(f)
    writer = csv.writer(ff)
    writer.writerow(next(reader))
    new_list = []
    for row in reader:
        if row[1] in uniq_repeated_email_list:
            new_list.append(row)
        elif row[1] not in uniq_repeated_email_list:
            writer.writerow(row)
    new_list1 = sorted(new_list, key=itemgetter(1))

    for row in new_list1:
        row[2] = convert_datetimestr_to_datetime(row[2])
    new_list2 = sorted(new_list1, key=itemgetter(1, 2))

    for counter, row in enumerate(new_list2, 1):
        if counter == len(new_list2):
            f.seek(0)
            reader = csv.reader(f)
            for value in reader:
                if value[0] == row[0]:
                    writer.writerow(value)
                    break
        elif row[1] != new_list2[counter][1]:
            f.seek(0)
            reader = csv.reader(f)
            for value in reader:
                if value[0] == row[0]:
                    writer.writerow(value)
    f.close()
    ff.close()


#testing
if __name__ == '__main__':
    write_last_log_to_csv('mail_log.csv', 'task_17_4_result.csv')