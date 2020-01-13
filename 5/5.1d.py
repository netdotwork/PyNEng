#!/home/user/virtenvs/pyneng-py3-1/bin/python3
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device = input("Enter device name: ")
keys = list(london_co[device].keys())
print(keys)
fact =  input("Enter device parameter {}".format(keys))
fact1 = fact.lower()
print(london_co[device].get(fact1, 'We dont have this parameter'))
