import os

with open('text.txt', 'w') as infile:
    infile.write('Mama myla ramu.')

with open('text.txt', 'r') as infile:
    my_dict = dict()
    all_count = 0
    for string in infile:
        for elem in list(string):
            if elem.lower() not in my_dict and elem.isalpha():
                my_dict[elem.lower()] = 1
                all_count += 1
            elif elem.lower() in my_dict and elem.isalpha():
                my_dict[elem.lower()] += 1
                all_count += 1
            else:
                continue

sorted_tuples = sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))
sorted_dict = {k: v for k, v in sorted_tuples}

with open('analysis.txt', 'w') as outfile:
    for key, value in sorted_dict.items():
        outfile.write(str(key) + ' ' + str("%.3f" % (value / all_count)) + '\n')