n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))

sym_n = 0
sym_k = 0

for i in str(n):
    sym_n += 1
    if i == '.':
        break

for i in str(k):
    sym_k += 1
    if i == '.':
        break

print('Первое число наоборот:', str(n)[sym_n - 2::-1] + '.' + str(n)[:sym_n - 1:-1])
print('Второе число наоборот:', str(k)[sym_k - 2::-1] + '.' + str(k)[:sym_k - 1:-1])
print('Сумма:',
      float(
            str(n)[sym_n - 2::-1] + '.' + str(n)[:sym_n - 1:-1])
      +
      float(
            str(k)[sym_k - 2::-1] + '.' + str(k)[:sym_k - 1:-1]))


