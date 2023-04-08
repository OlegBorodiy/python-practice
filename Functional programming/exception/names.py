with open('people.txt', 'w') as infile:
    infile.write('Kolya' + '\n')
    infile.write('Sa' + '\n')
    infile.write('Nastya' + '\n')
    infile.write('Oleg' + '\n')
    infile.write('Al')

num_string = 1
sum_sym = 0
log_file = open('log.txt', 'w')

with open('people.txt', 'r') as outfile:
    for string in outfile:
        try:
            if len(string.rstrip()) < 3:
                raise BaseException
            num_string += 1
            sum_sym += len(string.rstrip())
        except BaseException:
            print('Длина {}-ой строки меньше 3-х символов.'.format(num_string))
            log_file.write('Длина {}-ой строки меньше 3-х символов.'.format(num_string) + '\n')
            num_string += 1
            sum_sym += len(string.rstrip())

log_file.close()

print('Общее число символов:', sum_sym)