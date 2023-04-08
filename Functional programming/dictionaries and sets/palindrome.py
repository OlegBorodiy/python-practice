string = input('Введите строку: ')
new_string = string
flag = False

for i in range((len(string)) // 2):
    if new_string == new_string[::-1]:
        print('Можно сделать палиндромом')
        flag = True
        break
    else:
        new_string = string[i + 1:] + string[:i + 1]

if flag == False:
    new_string = string
    for i in range((len(string)) // 2):
        if new_string == new_string[::-1]:
            print('Можно сделать палиндромом')
            flag = True
            break
        else:
            new_string = string[- 1:i - 2:-1] + string[:len(string) - i - 1]

if flag == False:
    print('Нельзя сделать палиндромом')



# ####Пример 1:
# ````
# Введите строку: aab
# Можно сделать палиндромом
# ````
#
# ####Пример 2:
# ````
# Введите строку: aabc
# Нельзя сделать палиндромом
