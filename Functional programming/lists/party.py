guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришел или ушел? ')
    if answer != 'Пора спать':
        name_g = input('Имя гостя: ')
        if answer == 'пришел' and len(guests) <= 5:
            print('Привет,', name_g + '!')
            guests.append(name_g)
        elif answer == 'ушел' and len(guests) <= 6:
            print('Пока,', name_g + '!')
            guests.remove(name_g)
        else:
            print('Прости,', name_g, 'но мест нет.')
    else:
        print('\nВечеринка закончилась, все легли спать.')
        break

