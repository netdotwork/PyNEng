#!/home/user/virtenvs/pyneng-py3-1/bin/python3
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

mode = input("Enter interface mode (access/trunk): ")
mode1 = mode + '_template'
vlan_template = { 'access': 'Enter number of VLAN: ', 'trunk': 'Enter allowed VLANs: ' }
number = input("Enter interface type (Gi/Fa) and interface number (0/?): ")
vlan = input(vlan_template[mode])
template = { 'access_template': access_template, 'trunk_template': trunk_template }

print ('Interface {}'.format(number))
print('\n'.join(template[mode1]).format(vlan))
