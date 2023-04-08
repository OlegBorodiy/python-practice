import random

participants = 'Alex', 'Denver', 'Lucas', 'Jimmy', 'Sara', 'Dima'
prize_pool = {'Alex': [0, 0], 'Denver': [0, 0], 'Lucas': [0, 0],
              'Jimmy': [0, 0], 'Sara': [0, 0], 'Dima': [0, 0]}
name_result_dict = dict()

count_line = int(input('Сколько записей вносится в протокол? '))

print('Записи (результат и имя):')

for _ in range(count_line):
    result = int(str(random.randint(1, 9)) + str(random.randint(1, 9))
          + str(random.randint(1, 9)) + str(random.randint(1, 9))
          + str(random.randint(1, 9)))
    name = participants[random.randint(0, 5)]
    print(_ + 1, 'запись:', result, name)
    if result > prize_pool[name][1]:
        prize_pool[name][1] = result
        prize_pool[name][0] = _ + 1

# sorted_points = [points[1] for points in prize_pool.values()]
# sorted_points.sort(reverse=True)

sorted_tuples = sorted(prize_pool.items(), key=lambda item: item[1][1], reverse=True)
sorted_dict = {k: v for k, v in sorted_tuples}

print()
print('Итоги соревнований:')
for _ in range(3):
    print(_ + 1, 'место.', list(sorted_dict)[_], sorted_dict[list(sorted_dict)[_]][1])
