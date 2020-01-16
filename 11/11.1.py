with open('sh_cdp_n_sw1.txt') as f:
    f_line = f.read()
    #print(f_line)

def parse_cdp_neighbors(command_output):
    '''
    Функция принимает в качестве аргумента вывод "show cdp neighbors" (из файла) в виде строки.
    Функция возвращает словарь, который описывает соединения между устройствами:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'), ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
    Функцию можно еще оптимизировать, но нет :'(
    Целью также было научиться использовать генераторы списков, словарей  и полезные функции из раздела 10
    '''
    # получаем список всех устройств из вывода
    device_list = [word for word in command_output.split() if len(word) >= 2 and len(word) <= 8 and word[1].isdigit() and 'R' in word or 'SW' in word]
    #print(device_list, end = '\n' + '-' * 13 + '\n')
    # получаем структурированный список интерфейсов (сперва Local Interface, затем Port ID)
    interface_list = [word for word in command_output.split() if 'Eth' in word or '/' in word]
    # получаем список Local Interface
    interface_key_list =  [interface_list[i] + interface_list[i+1] for i in range(0, len(interface_list), 4)]
    # получаем список Local device (кол-во = кол-ву Local Interface для использования zip() дальше)
    device_key_list = [device_list[0][0:device_list[0].find('>')] for i in range(0, len(interface_key_list))]
    # получаем список Port ID
    interface_value_list =  [interface_list[i] + interface_list[i+1] for i in range(2, len(interface_list), 4)]
    # получаем список Device ID
    device_list.pop(0)
    # получаем списки из кортежей с помощью функции zip()
    f_key_list = list(zip(device_key_list, interface_key_list))
    f_value_list = list(zip(device_list, interface_value_list))
    #print(interface_list, end = '\n' + '-' * 13 + '\n')
    #print(device_key_list, end = '\n' + '-' * 13 + '\n')
    #print(interface_key_list, end = '\n' + '-' * 13 + '\n')
    #print(device_list, end = '\n' + '-' * 13 + '\n')
    #print(interface_value_list, end = '\n' + '-' * 13 + '\n')
    # выводим словарь, сформированный с помощью zip() из полученных ранее списков
    print(dict(zip(f_key_list, f_value_list)), end = '\n' + '-' * 13 + ' final ' + '-' * 13 + '\n')

# testing
parse_cdp_neighbors(f_line)