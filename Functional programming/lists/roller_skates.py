size_list = []
mem_list = []
amount = 0

size_am = int(input('Кол-во коньков: '))

for i in range(size_am):
    print('Размер', i + 1, 'пары:', end=' ')
    size = int(input())
    size_list.append(size)

print()

members = int(input('Кол-во людей: '))

for i in range(members):
    print('Размер ноги', i + 1, 'человека:', end=' ')
    size = int(input())
    mem_list.append(size)

size_list.sort()
mem_list.sort()

for index_mem in mem_list:
    for index_size in size_list:
        if index_mem <= index_size:
            size_list.remove(index_size)
            amount += 1
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', amount)

