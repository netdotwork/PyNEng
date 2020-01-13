ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
# сложно
#for list_command in ignore:
#    if list_command in str(command):
#        return True
#        break
#    else:
#        continue
#else:
#    return False

# проще
#for word in ignore:
#    if word in command:
#        return True
#return False

# очень просто и красиво
    return any(word in command for word in ignore)

config_dict = {}

def convert_config_to_dig(config_filename):
    '''
    Функция проверяет файл конфигурации построчно.
    Исключает строки, совпадающие со значениями списка ignore, даже частично.
    Выводит в виде словаря
    '''
    with open(r'{0}'.format(config_filename)) as f:
        for line in f:
            if ignore_command(line, ignore) or line[0] == '!':
                continue
            elif line[0] != ' ':
                key = line.strip()
                config_dict[key] = []
                continue
            elif line[0] == ' ':
                config_dict[key].append(line.strip())
        print(config_dict)


# testing
convert_config_to_dig('config_sw1.txt')