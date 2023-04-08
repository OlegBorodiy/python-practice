count = 1

string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')
new_string = string_2

while True:
    if string_1.startswith(new_string):
        print('\nПервая строка получается из второй со сдвигом', count - 1)
        break
    if count == len(string_1):
        print('Первую строку нельзя получить из второй'
              ' с помощью циклического сдвига.')
        break
    else:
        new_string = string_2[len(string_2) - count:len(string_2)] + \
                     string_2[count - count:len(string_2) - count]
        count += 1