def analysis(string_list, line):
    try:
        if len(string_list) == 0:
            print(f'Строка №{line} не содержит данных')
        if len(string_list) == 3:
            if not string_list[0].isdigit() or not string_list[2].isdigit():
                print(f'В строке №{line} не все данные являются цифрами')
            if '+' not in string_list[1] and '/' not in string_list[1] \
                    and '*' not in string_list[1] and '-' not in string_list[1]:
                print(f'В строке №{line} нет символа операции')
            else:
                if string_list[1] == '+':
                    return int(string_list[0]) + int(string_list[2])
                if string_list[1] == '/':
                    return int(string_list[0]) / int(string_list[2])
                if string_list[1] == '*':
                    return int(string_list[0]) * int(string_list[2])
                if string_list[1] == '-':
                    return int(string_list[0]) - int(string_list[2])
                else:
                    print(f'Строка №{line} не имеет корректного оператора')

    except:
        print(f'Неизвестная ошибка в строке №{line}')


sum_result = 0
number = 1


with open('calc.txt', 'r') as infile:
    for string in infile:
        data = string.split()
        result = analysis(data, number)
        number += 1
        if result != None:
            sum_result += result


print('Сумма результатов:', sum_result)