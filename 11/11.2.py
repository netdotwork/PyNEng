from create_dictionary import parse_cdp_neighbors
from draw_network_graph import draw_topology

map = {}
key_list = []

def create_network_map(*args):
    '''
    Функция create_network_map обрабатывает вывод команды show cdp neighbors
    из нескольких файлов и объединяет его в одну общую топологию.

    У функции должен быть один параметр filenames (вместо него *args),
    который ожидает как аргумент список с именами файлов, в которых находится
    вывод команды show cdp neighbors.

    С помощью функции draw_topology из файла draw_network_graph.py рисуем схему на основании
    топологии, полученной с помощью функции create_network_map.

    Результат помещается в 'img/topology'
    '''
    # открываем каждый файл как строку, формируем общий словарь из всех файлов-аргументов
    # с помощью функции parse_cdp_neighbors()
    for file in args:
        with open(file) as f:
            f_line = f.read()
            a = parse_cdp_neighbors(f_line)
            map.update(a)
    #print(map)
    # проверяем полученный словарь на дублирование ключей и значений, исключаем дубли
    # всё, что дублируется, помещаем в список key_list
    for key in map.keys():
        #print(map[key])
        for value in map.values():
            if key == value:
                key_list.append(key)
    #print(key_list)
    #print(int((len(key_list))/2))
    # теперь удаляем из списка key_list первую половину значений (например, первые 3 из списка из 6 значений)
    # т.к. нужно удалить только дублирующиеся значения, а не все повторяющиеся
    for i in range(0, int((len(key_list))/2)):
        key_list.pop(0)
    #print(key_list)
    for key1 in key_list:
        del map[key1]
    #print(map)
    # рисуем топологию в 'img/topology'
    draw_topology(map)

# testing
create_network_map('sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt')