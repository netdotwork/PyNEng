#with open('sh_cdp_n_sw1.txt') as f:
#    f_line = f.read()
#    print(f_line)
def parse_cdp_neighbors(command_output):
    '''
    Функцию можно еще оптимизировать, но нет :'(
    Целью было использовать генераторы списков, словарей  и полезные функции из раздела 10
    '''
    device_list = [word for word in command_output.split() if len(word) >= 2 and len(word) <= 8 and word[1].isdigit() and 'R' in word or 'SW' in word]
    interface_list = [word for word in command_output.split() if 'Eth' in word or '/' in word]
    interface_key_list =  [interface_list[i] + interface_list[i+1] for i in range(0, len(interface_list), 4)]
    device_key_list = [device_list[0][0:device_list[0].find('>')] for i in range(0, len(interface_key_list))]
    interface_value_list =  [interface_list[i] + interface_list[i+1] for i in range(2, len(interface_list), 4)]
    device_list.pop(0)
    f_key_list = list(zip(device_key_list, interface_key_list))
    f_value_list = list(zip(device_list, interface_value_list))
    return (dict(zip(f_key_list, f_value_list)))

if __name__ == '__main__':
    print(interface_list, end = '\n' + '-' * 13 + '\n')
    print(device_key_list, end = '\n' + '-' * 13 + '\n')
    print(interface_key_list, end = '\n' + '-' * 13 + '\n')
    print(device_list, end = '\n' + '-' * 13 + '\n')
    print(interface_value_list, end = '\n' + '-' * 13 + '\n')
    print(dict(zip(f_key_list, f_value_list)), end = '\n' + '-' * 13 + ' final ' + '-' * 13 + '\n')

# testing
#parse_cdp_neighbors(f_line)