config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

# delete first 29 symbols and transform our string to list-type (with separator ',') 
# and print it
print((config[30:]).split(','))
# alternative list from 1 element
print((config.split())[-1:])
