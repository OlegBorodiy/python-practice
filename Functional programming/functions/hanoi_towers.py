def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp)
        print("Переложить диск", n, "со стержня номер", start, "на стержень номер", finish)
        move(n - 1, temp, finish)

count = int(input("Введите количество дисков: "))
move(count, 1, 3)
