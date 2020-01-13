mac = 'AAAA:BBBB:CCCC'

# transform our string-type to list-type (with separator ':')
mac1 = mac.split(':')

# output for checking only
print(mac1)

# change separator ':' to '.' and print it 
# use .format-method and arguments of list to form a new string
print("{}.{}.{}".format(mac1[0], mac1[1], mac1[2]))
# alternative version
print('.'.join(mac1))
# alternative version
print(mac.replace(':', '.')) 
