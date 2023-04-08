students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def int_fam(dict):
    list_int = []
    sum_letters = 0
    for tuples in dict.values():
        list_int += tuples['interests']
        sum_letters += len(tuples['surname'])
    return list_int, sum_letters

def alone_var(stud):
    for key, values in stud.items():
        id = key
        name = values['name']
        surname = values['surname']
        age = values['age']
        interests = values['interests']
        print('Айди:', id, 'Имя:', name, 'Фамилия:', surname,
              'Возраст:', age, 'Интересы:', interests)

for key, value in students.items():
    print(key, value['age'])
print()

interests, letters = int_fam(students)
print(interests, letters, '\n')


alone_var(students)