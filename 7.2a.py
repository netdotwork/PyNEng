ignore = ['duplex', 'alias', 'Current configuration']
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
            if value == True or line[0] == '!':
                continue
            else:
                print(line.rstrip())
                continue