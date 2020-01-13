trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    Функция генерирует словарь для trunk-интерфейсов.
    В качестве ключей - интерфейсы.
    В качестве значений - команды из списка + номера vid из словаря (значения в виде списка)
    '''
    trunk_commands = {key: [] for key in intf_vlan_mapping.keys()}
    for key, value in intf_vlan_mapping.items():
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                trunk_commands[key].append(command + ' ' + str(value).strip('[]'))
            else:
                trunk_commands[key].append(command)
    else:
        print(type(trunk_commands))
        print(trunk_commands)

#testing
generate_trunk_config(trunk_config, trunk_mode_template)