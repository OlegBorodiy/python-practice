import os
from operator import itemgetter
all_list = list()

with open('first_tour.txt', 'r') as infile:
    for string in infile:
        if len(string) > 4:
            string_list = string.split(' ')
            if int(string_list[2]) > number_k:
                all_list.append(string_list)
        else:
            number_k = int(string)

participants_sorted = sorted(all_list, key=itemgetter(2), reverse=True)

with open('second_tour.txt', 'w') as outfile:
    outfile.write(str(len(participants_sorted)) + '\n')
    for _ in range(len(participants_sorted)):
        outfile.write(str(_ + 1) + ') ' + participants_sorted[_][1][0:1] + '. ' +
                      participants_sorted[_][0] + ' ' + participants_sorted[_][2])

