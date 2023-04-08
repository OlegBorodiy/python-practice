def print_dict(d, indent=4):
    for key, value in d.items():
        if isinstance(value, dict):
            print(' ' * indent + "'" + str(key) + "'" + ': ' + '{')
            print_dict(value, indent+4)
        else:
            print(' ' * indent + "'" + str(key) + "'" + ': ' + "'" + str(value) + "'")
    if key == 'title':
        print(' ' * (indent - 4) + "},")
    else:
        print(' ' * (indent - 4) + "}")
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


step = int(input('Сколько сайтов: ')) #Вводим количество сайтов

for _ in range(step): #Запускаем цикл, в котором меняем переменную имени продукта
    name = input('Введите название продукта для нового сайта: ')
    site['html']['head']['title'] = f'Куплю/продам {name} недорого'
    site['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
    print()
    print(f'Сайт для {name}:') #Перед выводом самого сайта выводим название
    print('site = {')
    print_dict(site) #Вызываем функцию, которая должна напечатать содержимое сайта,
    # передаём в неё уже изменённый для продукта текст

