template = '''
{0:4}    {1}    {2}
'''
sorted_list = []
with open(r'Absolute_path_to_file\CAM_table.txt') as f:
    i = 0
    for line in f:
        if i < 6:
            i += 1
            continue
        else:
            list = line.split()
            sorted_list.append(template.format(int(list[0]), list[1], list[3]).strip('\n'))
    else:
        sorted_list.sort()
        for line_sorted_list in sorted_list:
            print(line_sorted_list)