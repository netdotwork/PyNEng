interface_list = []
access_dict = {}
trunk_dict = {}
def get_int_vlan_map(config_filename):
    '''
    Функция отображает набор интерфейсов и настроенных vid в виде словаря.
    Для access-интерфейсов выводит все vid, не включая 1.
    Для trunk-интерфейсов выводит vid в виде списка значений
    '''
    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if line.startswith('interface F'):
                key = line
            elif line.startswith(' switchport access'):
                access_dict.update({key.strip(): int(line[23::].strip())})
            elif line.startswith(' switchport trunk allowed'):
                trunk_dict.update({key.strip(): line[30::].strip().split(',')})
        print(tuple([access_dict, trunk_dict]))

#testing
get_int_vlan_map('config_sw1.txt')