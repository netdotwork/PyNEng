access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

access_commands = []

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    '''
    Функция возвращает шаблон конфигурации для access-интерфейсов.
    Номера vid указаны в виде значений словаря, передаваемого функции.
    В зависимости от параметра psecurity для каждого интерфейса добавляются или нет настройки port security
    '''
    for key, value in intf_vlan_mapping.items():
        access_commands.append('interface ' + key)
        for command in access_template:
            if command.startswith('switchport access'):
                access_commands.append(command + ' ' + str(value))
            else:
                access_commands.append(command)
        if psecurity == True:
            for command in port_security_template:
                access_commands.append(command)
    else:
        print(access_commands)

#testing
generate_access_config(access_config, access_mode_template)
access_commands = []
generate_access_config(access_config, access_mode_template, psecurity=True)