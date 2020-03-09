# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    '''
    Функция отображает набор интерфейсов и настроенных vid в виде словаря.
    Для access-интерфейсов выводит все vid, включая 1.
    Для trunk-интерфейсов выводит vid в виде списка значений
    '''
    interface_list = []

    access_dict = {}

    trunk_dict = {}

    all_dict = {}

    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if line.startswith('interface F'):
                key = line.lstrip('interface')
                interface_list.append(key.strip())
            elif line.startswith(' switchport access'):
                all_dict.update({key.strip(): int(line[23::].strip())})
                access_dict.update({key.strip(): int(line[23::].strip())})
            elif line.startswith(' switchport trunk allowed'):
                all_dict.update({key.strip(): [int(i) for i in line[30::].split(',')]})
                trunk_dict.update({key.strip(): [int(i) for i in line[30::].split(',')]})
        all_list = list(all_dict.keys())
        for value in interface_list:
                for i in range(0, len(all_list)):
                    if value == all_list[i]:
                        break
                    else:
                        if i == len(all_list) - 1:
                            access_dict[value] = 1
                        else:
                            continue
        return(tuple([access_dict, trunk_dict]))

#testing
print(get_int_vlan_map('config_sw2.txt'))