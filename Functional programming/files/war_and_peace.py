import os, zipfile
extract_dir = 'extract_dir'

with zipfile.ZipFile('voyna-i-mir.zip') as zf:
    zf.extractall(extract_dir)

my_path = os.path.abspath(os.path.join('extract_dir', 'voyna-i-mir.txt'))
with open(my_path, 'r', encoding='utf-8') as infile:
    print(os.path.abspath(os.getcwd()))
    my_dict = dict()
    all_count = 0
    for string in infile:
        for elem in list(string):
            if elem.lower() not in my_dict and elem.isalpha():
                my_dict[elem.lower()] = 1
            elif elem.lower() in my_dict and elem.isalpha():
                my_dict[elem.lower()] += 1
            else:
                continue

sorted_tuples = sorted(my_dict.items(), key=lambda item: -item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

with open('analysis.txt', 'w') as outfile:
    for key, value in sorted_dict.items():
        outfile.write(str(key) + ' ' + str(value) + ' раз' + '\n')