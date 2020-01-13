trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

trunk_commands = []

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    Функция генерирует список для trunk-интерфейсов.
    В качестве значений - интерфейсы и перечень команд с учетом номеров vid
    '''
    for key, value in intf_vlan_mapping.items():
        trunk_commands.append('interface ' + key)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                trunk_commands.append(command + ' ' + str(value).strip('[]'))
            else:
                trunk_commands.append(command)
    else:
        print(trunk_commands)

#testing
generate_trunk_config(trunk_config, trunk_mode_template)