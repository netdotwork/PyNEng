vlan = input('Please enter vlan id: ')
template = '''
{0:4}    {1}    {2}
'''

with open(r'Absolute_path_to_file\CAM_table.txt') as f:
    i = 0
    for line in f:
        if i < 6:
            i += 1
            continue
        else:
            list = line.split()
            if list[0] == vlan:
                print(template.format(list[0], list[1], list[3]).strip('\n'))
            else:
                continue