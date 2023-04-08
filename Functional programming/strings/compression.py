string = input('Введите строку: ')
last_sym = string[0]
count = 0
new_string = ''

for sym in string:
    if sym == last_sym:
        count += 1
        last_sym = sym
    else:
        new_string += last_sym + str(count)
        last_sym = sym
        count = 1
new_string += last_sym + str(count)

print('Закодированная строка:', new_string)

