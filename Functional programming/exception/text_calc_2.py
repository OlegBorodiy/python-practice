def operator(old_string, string_list):
    try:
        if string_list[1] == '+':
            return int(string_list[0]) + int(string_list[2])
        if string_list[1] == '/':
            return int(string_list[0]) / int(string_list[2])
        if string_list[1] == '*':
            return int(string_list[0]) * int(string_list[2])
        if string_list[1] == '-':
            return int(string_list[0]) - int(string_list[2])
    except:
        operator_result = analysis(old_string, string_list)
        return operator_result

def analysis(my_string, my_list):
    print('Обнаружена ошибка в строке:', my_string, end=' ')
    question = input('Хотите исправить? ').lower()
    if question == 'да':
        new_string = input('Введите исправленную строку: ')
        new_data = new_string.split()
        operator(new_string, new_data)


sum_result = 0

with open('calc.txt', 'r') as infile:
    for string in infile:
        data = string.split()
        result = operator(string, data)
        if result != None:
            sum_result += result

print('Сумма результатов:', sum_result)