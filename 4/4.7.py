mac = 'AAAA:BBBB:CCCC'

# transform string-type to list-type (separator ':')
mac1 = mac.split(':')

# output for checking only
#print(mac1)

# transform back form list-type to string-type (without separator)
mac2 = ''.join(mac1)

# output for checking only
#print(mac2)

# output for checking only
#print(type(mac2))

# trasnform string-type to int-type and binary (AAAABBBBCCCC - 16)
int1 = bin(int(mac2, 16))

# print number int1 and delete 0b
print(int1.strip('0b'))
# alternative version
print((bin(int(mac2, 16)).strip('0b'))) 
