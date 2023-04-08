import random

count = int(input('Количество палок: '))
push_count = int(input('Количество бросков: '))

count_list = [_ for _ in range(1, count + 1)]

for push in range(push_count):
    left = random.randint(1, count)
    right = random.randint(1, count)
    if left > right:
        left, right = right, left
    l_and_r = [_ for _ in range(left, right + 1)]
    print('Бросок', str(push + 1) + '. Сбиты палки с номера', left,
          'по номер', right)
    for i in range(left, right + 1):
        count_list[i - 1] = '.'

new_list = ['.' if elem == '.' else 'I' for elem in count_list]

print(new_list)