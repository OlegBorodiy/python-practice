def search(data, key_user, level=None):
    if level is None or level >= 1:
        if key_user in data:
            return data[key_user]
    else:
        return None
    for val in data.values():
        if isinstance(val, dict) and level is not None:
            result = search(val, key_user, level - 1)
            if result:
                break
        if isinstance(val, dict) and level is None:
            result = search(val, key_user, level)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


key = input('Введите искомый ключ: ')
question = input('Хотите ли ввести глубину поиска? (Да/Нет): ').lower()
if question == 'да':
    step = int(input('Какая глубина? '))
    answer = search(site, key, step)
else:
    answer = search(site, key)

if answer is None:
    print('Нет такого ключа!')
else:
    print(f'Значение ключа: {answer}')
