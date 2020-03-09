# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

mode = input("Enter interface mode (access/trunk): ")
mode1 = mode + '_template'
vlan_template = { 'access': 'Enter number of VLAN: ', 'trunk': 'Enter allowed VLANs: ' }
number = input("Enter interface type (Gi/Fa) and interface number (0/?): ")
vlan = input(vlan_template[mode])
template = { 'access_template': access_template, 'trunk_template': trunk_template }

print ('Interface {}'.format(number))
print('\n'.join(template[mode1]).format(vlan))