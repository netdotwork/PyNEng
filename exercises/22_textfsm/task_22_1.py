# -*- coding: utf-8 -*-
"""
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

"""
import textfsm

def parse_command_output(template, command_output):
    #template_dir, template_file = os.path.split(template)
    with open(template, encoding = 'UTF-8') as f:
        fsm = textfsm.TextFSM(f)
        header = fsm.header
        result = fsm.ParseText(command_output)
        result.insert(0, header)
        return result


#testing
if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt", encoding = 'UTF-8') as ff:
        sh_ip_int_br_as_line = ff.read()
        print(parse_command_output("templates/sh_ip_int_br.template", sh_ip_int_br_as_line))