symbol_count = 0

while True:
    user_name = input('Введите имя пользователя: ')
    user_sym = len(user_name) + 1

    print('Выберете действие:\n', '1. Посмотреть текущий текст чата\n', '2. Отправить сообщение\n')

    action = int(input())

    if action == 1:
        print('История чата:')
        with open('history_chat.txt', 'r') as readfile:
            for string in readfile:
                print(string)
    elif action == 2:
        user_message = input('Введите своё сообщение: ')
        with open('history_chat.txt', 'a') as writefile:
            writefile.write(user_name + ': ' + user_message + '\n')
            symbol_count += user_sym + len(user_message) + 1
            writefile.seek(symbol_count)
    else:
        print('Введён неверный выбор!')
        print()


