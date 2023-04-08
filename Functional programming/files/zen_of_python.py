import os

alph_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
             'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
             'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
             'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
             'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
             'z': 0}

file = open(os.path.abspath('ABSPATH'), 'r')

string_count = 0
words_count = 0
liters_count = 0

for string in file:
    string_count += 1
    for words in string.split(' '):
        words_count += 1
        for symbol in list(words):
            if symbol.isalpha():
                liters_count += 1
                alph_dict[symbol.lower()] += 1

sorted_dict = dict(sorted(alph_dict.items(), key=lambda item: item[1]), reverse=True)


print('Количество строк:', string_count)
print('Количество слов:', words_count)
print('Количество букв:', liters_count)
print('Буква, которая встречается в тексте наименьшее количество раз это:', end=' ')

for key, value in sorted_dict.items():
    print(key, '-', value, 'раз')
    break