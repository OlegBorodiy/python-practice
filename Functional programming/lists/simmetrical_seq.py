count_coup = 1
list_numb = []
numbers_list = []

amount = int(input('Кол-во чисел: '))

for elem in range(amount):
    number = int(input('Число: '))
    list_numb.append(number)

print('Последовательность:', list_numb)

for index in range(amount - 1):
    if list_numb[amount - index - 1] == list_numb[amount - index - 2]:
        count_coup += 1
    else:
        break

numbers_list.extend(list_numb[:-count_coup:][::-1])

print('Нужно приписать чисел:', amount - count_coup)
print('Сами числа:', numbers_list)