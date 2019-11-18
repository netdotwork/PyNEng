ip = input('Please enter ip address: ')
ip_list = ip.split('.')
if int(ip_list[0]) >= 1 and int(ip_list[0]) <= 223:
    print("it's unicast")
elif int(ip_list[0]) >= 224 and int(ip_list[0]) <= 239:
    print("it's multicast")
elif int(ip_list[0]) == 255:
    i = 1
    octet = int(ip_list[i])
    while octet == 255 and i < 3:
        i += 1
        octet = int(ip_list[i])
    else:
        if i == 3:
            print ("it's local broadcast")
        else:
            print("it's unused")
elif int(ip_list[0]) == 0:
    for n in range(1, 3):
        if int(ip_list[n]) == 0:
            continue
        else:
            print("it's unused")
            break
    print("it's anassigned")
else:
    print("it's unused, dude!")