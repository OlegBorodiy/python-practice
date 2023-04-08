import random


class Student:
    name_list = ['Kolya', 'Nastya', 'Petya', 'Patrik']
    sur_name_list = ['Border', 'Petrov', 'Ivanov', 'Shekland']

    def __init__(self):
        self.name = Student.name_list[random.randint(0, 3)]
        self.sur_name = Student.sur_name_list[random.randint(0, 3)]
        self.num_group = random.randint(1, 5)
        self.five_elem = [random.randint(1, 5) for _ in range(5)]
        self.ranking = sum(self.five_elem) / 5

    def return_value(self):
        return self.sur_name, self.name, self.num_group, self.five_elem, self.ranking


all_student_list = list()

for _ in range(10):
    new_student = Student()
    data = new_student.return_value()
    all_student_list.append(data)

sorted_student = sorted(all_student_list, key=lambda x: x[4])


print('{:_^11}{:_^10}{:_^12}{:_^13}{:_^14}'.format('Фамилия', 'Имя', 'Номер группы', 'Оценки', 'Средний балл'))

for tuples in sorted_student:
    for lists in tuples:
        if isinstance(lists, list):
            for num in lists:
                print('{:^2}'.format(num), end=' ')
        else:
            print('{:^10}'.format(lists), end=' ')
    print()