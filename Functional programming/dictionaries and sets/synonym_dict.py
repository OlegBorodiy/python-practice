coupl_dict = dict()

count = int(input('Введите количество пар слов: '))

for _ in range(count):
    print(_ + 1, 'пара: ', end='')
    coupl = input().lower().split(' - ')
    coupl_dict[coupl[0]] = coupl[1]


while True:
    syn = ''
    words = input('Введите слово: ').lower()
    if words not in coupl_dict.keys() and words not in coupl_dict.values():
        print('Такого слова в словаре нет.')
    else:
        if words in coupl_dict.keys():
            syn = coupl_dict[words]
            break
        elif words in coupl_dict.values():
            syn = [key[0] for key in coupl_dict.items() if key[1] == words]
        break

print('Синоним:', syn[0].title())
