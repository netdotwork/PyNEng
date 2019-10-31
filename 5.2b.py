#!/home/user/virtenvs/pyneng-py3-1/bin/python3
# works fot 192.168.1.1/24, but doesn't work for prifixes like 10.1.1.0/24, because 10 = 0b1010, but we need to get 0b00001010
from sys import argv
#ip = input("Enter your ip address with mask, please: ")
ip =argv[1]
ip1 = ip.split('/')
ip2 = ip1[0].split('.')
ip3 = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(ip2[0]), int(ip2[1]), int(ip2[2]), int(ip2[3]))
mask = '1' * int(ip1[1]) + '0' * (32-int(ip1[1]))
network = int(ip3, 2) & int(mask, 2)
network1 = bin(network)
network2 = str(network1)

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template.format(int(network2[2:10], 2), int(network2[10:18], 2), int(network2[18:26], 2), int(network2[26::], 2)))

mask1 = ip[ip.find('/')::]

mask_template = '''
Mask:
{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:<08b} {2:<08b} {3:<08b} {4:<08b}
'''
print(mask_template.format(mask1, int(mask[0:8], 2), int(mask[8:16], 2), int(mask[16:24], 2), int(mask[24::], 2)))
