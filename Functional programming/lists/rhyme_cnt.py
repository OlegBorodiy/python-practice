amount_mem = int(input('Кол-во человек: '))
step_num = int(input('Какое число в считалке? '))
last_i = 0

print('Значит, выбывает каждый', step_num, 'человек')

mem_list = list(range(1, amount_mem + 1))

while len(mem_list) != 1:
    print('\nТекущий круг людей:', mem_list)
    print('Начало счёта с номера', mem_list[last_i])

    last_i = step_num % len(mem_list) + last_i - 1

    print('Выбывает человек под номером', mem_list[last_i])

    mem_list.remove(mem_list[last_i])

    if last_i == len(mem_list):
        last_i = 0

print('Остался человек под номером', mem_list[0])