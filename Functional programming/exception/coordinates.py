import random
def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y
def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

outfile = open('result.txt', 'w')
step = 'с первой функцией'

with open('coordinates.txt', 'r') as infile:
    for line in infile:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            step = 'со второй функцией'
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            step = ''
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            for elem in my_list:
                outfile.write(str(elem) + ' ')
            outfile.write('\n')
        except:
            print("Что-то пошло не так {}".format(step))
    outfile.close()
