import os

user_line = input('Введите строку: ')
user_path = input('Куда хотите сохранить документ? '
                  'Введите последовательность папок (через пробел): ').split(' ')
print()
name_file = input('Введите имя файла: ')

abs_path = '/home/'

for elem in user_path:
    abs_path = os.path.join(abs_path, elem)

if name_file not in os.listdir(os.path.join('..', abs_path)):
    new_file = open(os.path.join(abs_path, name_file), 'w')
    new_file.write(user_line)
    new_file.close()
    print('Файл успешно сохранён!', '\n', '````','\n', '_Содержимое файла:_',user_line)
else:
    question = input('Вы действительно хотите перезаписать файл? ').lower()
    if question == 'да':
        new_file = open(os.path.join(abs_path, name_file), 'w')
        new_file.write(user_line)
        new_file.close()
        print('Файл успешно перезаписан!', '\n', '````', '\n', '_Содержимое файла:_', user_line)
