diction = dict()
revers_dict = dict()
text = sorted(input('Введите текст: '))

print('Оригинальный словарь частот: ')

last_sym = text[0]
count = 0

for sym in text:
    if sym == last_sym:
        count += 1
    else:
        diction[last_sym] = count
        print(last_sym, ':', count)
        last_sym = sym
        count = 1
diction[last_sym] = count
print(last_sym, ':', count)

print('\nИнвертированный словарь частот:')
val = set(diction.values())

for key in val:
    sum_keys = {}
    sum_values = []
    for value in diction.items():
        if key == value[1]:
            sum_values.append(value[0])
        sum_keys[key] = sum_values
    print(key, ':', sum_values)
    revers_dict.update(sum_keys)