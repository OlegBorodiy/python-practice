ip_adress = input('Введите IP: ')
list_adress = ip_adress.split('.')

if len(list_adress) != 4:
    print('Адрес - это четыре числа, разделенные точками')

else:
    for i in list_adress:
        if not i.isdigit():
            print(i, '- не целое число')
            break
        elif int(i) > 255:
            print(i, 'превышает 255')
            break
        elif list_adress[3] == i:
            print('IP-адрес корректен')
