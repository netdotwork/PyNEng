template = '''
Protocol:              {0}
Prefix:                {1}
AD/Metric:             {2}
Next-Hop:              {4}
Last update:           {5}
Outbound Interface:    {6}
'''

with open(r'Absolute_path_to_file\ospf.txt') as f:
    for file in f:
        list = file.split()
        print(template.format(list[0], list[1], list[2].strip('[]'), list[3], list[4], list[5], list[6]).rstrip())