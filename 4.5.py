command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

# keep only numbers and transform strings to list-type (with ',' separator)
command3 = command1[30:].split(',')
command4 = command2[30:].split(',')

# output for checking only
#print(command3)
#print(command4)

# transform our lists to tuple-type
set1 = set(command3)
set2 = set(command4)

# output for checking only
#print(set1)
#print(set2)

# find similar numbers in our tuples
duplicate_set = set1.intersection(set2)
#print(duplicate_set)

# transform tuple to list and sort it
list1 = list(duplicate_set)
list1.sort()

# output
print(list1)
