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

def generate_access_config(intf_vlan_mapping, access_template):
    '''
    Функция возвращает список access-интерфейсов и команд конфигурации.
    Функция в качестве аргумента принимает словарь с интерфейсами и номерами vid, а также список команд.
    '''
    for key, value in intf_vlan_mapping.items():
        access_commands.append('interface ' + key)
        for command in access_template:
            if command.startswith('switchport access'):
                access_commands.append(command + ' ' + str(value))
            else:
                access_commands.append(command)
    else:
        print(access_commands)

#testing
generate_access_config(access_config, access_mode_template)