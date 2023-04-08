box_list = []
amount = int(input('Кол-во контейнеров: '))

while amount != 0:
    box = int(input('Введите вес контейнера: '))
    if box % 1 == 0 and box < 200:
        amount -= 1
        box_list.append(box)
    else:
        print('Ошибка ввода')
        amount += 1

print()

new_box = int(input('Введите вес нового контейнера: '))
box_list.append(new_box)
box_list.sort(reverse=True)

position = box_list.index(new_box) + 1

if box_list.count(new_box) > 1:
    position += box_list.count(new_box) - 1
print('Номер, куда встанет новый контейнер:', position)