access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

access_commands = []

def generate_access_config(**kwargs):
    '''
    Функция возвращает список access-интерфейсов и команд конфигурации.
    Функция НЕ СООТВЕТСТВУЕТ ЗАДАНИЮ, т.к. в качестве аргумента ждет только словарь (а нужно еще и список команд).
    Функция использует параметр **kwargs для использования ключевых аргументов произвольной длины.
    КОРРЕКТНАЯ ФУНКЦИЯ, СООТВЕТСТВУЮЩАЯ ЗАДАНИЮ - 9.1_v1.py
    '''
    for key, value in kwargs.items():
        access_commands.append('interface ' + key)
        for command in access_mode_template:
            if command.startswith('switchport access'):
                access_commands.append(command + ' ' + str(value))
            else:
                access_commands.append(command)
    else:
        return access_commands

# testing
# **access_config - распаковываем словарь access_config
print(generate_access_config(**access_config))