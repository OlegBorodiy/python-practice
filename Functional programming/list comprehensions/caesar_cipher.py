alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
            'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

message = input('Введите сообщение: ')
move = int(input('Введите сдвиг: '))
new_message = [alphavit[alphavit.index(i) + move - 33]
               if i != ' '
               else ' '
               for i in message]

print('Зашифрованное сообщение: ', end='')

for sym in new_message:
    print(sym, end='')