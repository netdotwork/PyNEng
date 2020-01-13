ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

# transform our string-type to list-type (separator is many spaces)
list1 = ospf_route.split()

# output for checking only
#print(list1)

# form template for new string (use .format method and delete excess symbols like ',')
str1 = '''
Protocol:           OSPF
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''

# output of our template like new string with arguments from our list1
print(str1.format(list1[1], list1[2], list1[4].strip(','), list1[5].strip(','), list1[6]))
