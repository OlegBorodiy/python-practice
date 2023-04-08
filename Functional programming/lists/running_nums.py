old_list = [1, 4, -3, 0, 10]
move = int(input('Сдвиг: '))

print('Изначальный список:', old_list)
print('Сдвинутый список:', old_list[-move: len(old_list):]
      + old_list[:len(old_list) - move:])

