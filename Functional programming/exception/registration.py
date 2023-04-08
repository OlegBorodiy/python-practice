def analysis(string_list):
    if len(string_list) == 0:
        return IndexError
    if len(string_list) == 3:
        if not string_list[0].isalpha():
            return NameError
        if '@' and '.' not in string_list[1]:
            return SyntaxError
        if int(string_list[2]) > 99 or int(string_list[2]) < 10:
            return ValueError
        else:
            return True


bad_log = open('registrations_bad.log', 'w')
good_log = open('registrations_good.log', 'w')

with open('registrations.txt', 'r') as infile:
    for string in infile:
        data = string.split()
        flag = analysis(data)
        if flag == IndexError:
            bad_log.write(string.rstrip() + (' ' * 5) + 'НЕ присутствуют все три поля' + '\n')
        if flag == NameError:
            bad_log.write(string.rstrip() + (' ' * 5) + 'поле имени содержит НЕ только буквы' + '\n')
        if flag == SyntaxError:
            bad_log.write(string.rstrip() + (' ' * 5) + 'поле емейл НЕ содержит @ и .(точку)' + '\n')
        if flag == ValueError:
            bad_log.write(string.rstrip() + (' ' * 5) + 'поле возраст НЕ является числом от 10 до 99' + '\n')
        if flag == True:
            good_log.write(string.rstrip() + '\n')

bad_log.close()
good_log.close()