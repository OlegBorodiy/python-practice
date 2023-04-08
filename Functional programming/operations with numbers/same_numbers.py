first = int(input('Введите первый год: '))
second = int(input('Введите второй год: '))

print('\n''Года от', first, 'до', second, 'с тремя одинаковыми цифрами:')

for i in range(first, second + 1):
    i = str(i)
    if (i[0] == i[2] == i[3]) or (i[1] == i[2] == i[3]):
        print(i)
