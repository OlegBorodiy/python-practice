tel_dict = {
    ('Сидоров', 'Никита'):375256440011, ('Смирнова', 'Алина'):80441112342,
    ('Кулик', 'Павел'):80087623442, ('Петров', 'Алексей'):8763452321,
    ('Журикова', 'Жанна'):122341721, ('Ласточкин', 'Сергей'):98765431232
}


while True:
    print('Выберете действие:', '\n', '1 - добавить контакт', '2 - поиск человека по фамилии')
    question = int(input())
    if question == 1:
        print('Введите имя и фамилию через пробел:', end=' ')
        name, surname = input().split()
        print('Введите номер телефона:', end=' ')
        number = int(input())
        surname_name = surname.lower(), name.lower()
        flag = False
        for tel_surname, tel_name in tel_dict:
            tel_surname_name = tel_surname.lower(), tel_name.lower()
            if surname_name == tel_surname_name:
                print('Такой контакт уже есть в записной!')
                flag = True
                break
        if flag == False:
            tel_dict[(surname, name)] = number
            print('Текущий словарь контактов:')
            print(tel_dict)
    if question == 2:
        flag = False
        print('Введите фамилию для поиска:', end=' ')
        family = input().lower()
        for tel_surname, tel_name in tel_dict:
            if tel_surname.lower() == family:
                print(tel_surname, tel_name, number)
                flag = True
        if flag == False:
            print('Такого контакта нет в записной!')


