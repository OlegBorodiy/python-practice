first_list = []
second_list = []

for i in range(3):
    print('Введите', i + 1, 'число', end=' ')
    number = int(input())
    first_list.append(number)

for i in range(7):
    print('Введите', i + 1, 'число', end=' ')
    number = int(input())
    second_list.append(number)

print('Первый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

for elem in first_list:
    for _ in range(first_list.count(elem) - 1):
        first_list.remove(elem)

print('\nНовый первый список с уникальными элементами:', first_list)