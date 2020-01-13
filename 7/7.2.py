with open(r'Absolute_path_to_file\config_sw1.txt') as f:
    for line in f:
        if line[0] == '!':
            continue
        else:
            print(line.rstrip())