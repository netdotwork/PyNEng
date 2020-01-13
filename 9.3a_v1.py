interface_list = []
access_dict = {}
trunk_dict = {}
all_dict = {}
def get_int_vlan_map(config_filename):
    '''
    Функция отображает набор интерфейсов и настроенных vid в виде словаря.
    Для access-интерфейсов выводит все vid, включая 1.
    Для trunk-интерфейсов выводит vid в виде списка значений
    '''
    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if line.startswith('interface F'):
                key = line
                interface_list.append(key.strip())
            elif line.startswith(' switchport access'):
                all_dict.update({key.strip(): int(line[23::].strip())})
                access_dict.update({key.strip(): int(line[23::].strip())})
            elif line.startswith(' switchport trunk allowed'):
                all_dict.update({key.strip(): line[30::].strip().split(',')})
                trunk_dict.update({key.strip(): line[30::].strip().split(',')})
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
        print(tuple([access_dict, trunk_dict]))

#testing
get_int_vlan_map('config_sw2.txt')