NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

# use replace-method (for strings) for replace'Fast' on 'Gigabit' and print it
print(NAT.replace('Fast', 'Gigabit'))
