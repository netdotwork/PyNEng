interface_list = []

def get_int_vlan_map(config_filename):
    '''
    Функция отображает набор интерфейсов и настроенных vid в виде словаря.
    Для access-интерфейсов выводит все vid, не включая 1.
    Для trunk-интерфейсов выводит vid в виде списка значений.
    Это НЕКОРРЕКТНАЯ ФУНКЦИЯ - если номера vid совпадают для нескольких интерфейсов, то на вывод попадет только один из них.
    Сохраняю как пример использования генератора словарей.
    Рабочий пример - 9.3_v1.py
    '''
    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if line.startswith('interface F'):
                interface_list.append(line.rstrip())
            elif line.startswith(' switchport access') or line.startswith(' switchport trunk allowed'):
                interface_list.append(line.rstrip().strip())
            access_dict = {interface_list[interface_list.index(value)-1]: int(value[23::]) for value in interface_list if 'access' in value}
            trunk_dict = {interface_list[interface_list.index(value)-1]: value[30::].split(',') for value in interface_list if 'trunk' in value}
        access_trunk_list = [access_dict, trunk_dict]
        print(tuple(access_trunk_list))

#testing
get_int_vlan_map('config_sw1.txt')