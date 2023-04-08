import random

sum_num = 0
const_random = random.randint(1,13)

outfile = open('out_file.txt', 'w')

try:
    while sum_num < 777:
        number = int(input('Введите число: '))
        sum_num += number
        new_random = random.randint(1, 13)
        if new_random == const_random:
            raise BaseException
        outfile.write(str(number) + '\n')
except BaseException:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
finally:
    outfile.close()
