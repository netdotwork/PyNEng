# -*- coding: utf-8 -*-
"""
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
"""

import textfsm


def parse_output_to_dict(template, command_output):
    with open(template, encoding = 'UTF-8') as f:
        fsm = textfsm.TextFSM(f)
        header = fsm.header
        result = fsm.ParseText(command_output)
        output_list = [dict(zip(header, r)) for r in result]
        #output_list = []
        #for r in result:
            #output_list.append(dict(zip(header, r)))
        return output_list

#testing
if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt", encoding = 'UTF-8') as ff:
        sh_ip_int_br_as_line = ff.read()
        print(parse_output_to_dict("templates/sh_ip_int_br.template", sh_ip_int_br_as_line))