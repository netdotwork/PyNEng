# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
from jinja2 import Environment, FileSystemLoader
import yaml
import os


def generate_config(template, data_dict):
    template_dir, template_file = os.path.split(template)
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    j2_template = env.get_template(template_file)

    return j2_template.render(data_dict)


#testing
if __name__ == "__main__":
    template1 = "templates/for.txt"
    with open('data_files/for.yml') as f:
        data_dict1 = yaml.safe_load(f)
        print(generate_config(template1, data_dict1))