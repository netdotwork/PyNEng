ignore = ['duplex', 'alias', 'Current configuration']
cfg_list = []
with open(r'Absolute_path_to_file\config_sw1.txt') as f:
    for line in f:
        value = False
        i = 0
        while i < 3 and not value:
            if not line.startswith(ignore[i]) and not line.startswith(' ' + ignore[i]):
                i += 1
                continue
            else:
                i = 3
                value = True
        else:
            if value == True:
                continue
            else:
                cfg_list.append(line)
                continue
f1 = open(r'Absolute_path_to_file\config_sw1_cleared.txt', 'w')
f1.writelines(cfg_list)
f1.close()