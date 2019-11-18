trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
if trunk and trunk_template:
    x = len(trunk_template)
    for key, value in trunk.items():
        if x > 0:
            print('Interface FastEthernet' + key)
            x = 0
        else:
            print('\nInterface FastEthernet' + key)
        for command in trunk_template:
            x -= 1
            if command.endswith('allowed vlan'):
                a = len(value)
                b = 0
                while b < a:
                    command += ' ' + value[b]
                    b += 1
                else:
                    print('{}'.format(command))
            else:
                print('{}'.format(command))
else:
    print('Empty :(')