import os
def search_file(path_abs, size=['0'], catalogs=['0'], files=['0']):
    for elem in os.listdir(path_abs):
        new_path = os.path.join(path_abs, elem)
        if os.path.isdir(new_path):
            catalogs[0] = int(catalogs[0]) + 1
            search_file(new_path, size, catalogs, files)
        else:
            files[0] = int(files[0]) + 1
            size[0] = int(size[0]) + os.path.getsize(new_path)
    return size, catalogs, files

user_path = os.path.abspath('ABSPATH')

sum_size, count_catalogs, count_files = search_file(user_path)

print('Размер каталога (в Кб):', float(sum_size[0]) / 1024)
print('Количество подкаталогов:', int(count_catalogs[0]))
print('Количество файлов:', int(count_files[0]))