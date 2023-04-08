import random
class Parents:
    def __init__(self, name, age, list_kids):
        self.name = name
        self.age = age
        self.list_kids = list_kids

    def info(self):
        print(f'Информация о родителе {self.name}:\nВозраст: {self.age}\nСписок детей:', end=' ')
        for name in self.list_kids:
            print(f'{name}', end=' ')
        print('\n')

class Child:
    def __init__(self, name, parent_age):
        self.name = name
        self.age = random.randint(1, parent_age - 16)
        self.state = 'Не спокоен'
        self.hunger = 'Голоден'

    def kids_info(self):
        print(f'Информация о ребёнке {self.name}:\n'
              f'Возраст: {self.age}\n'
              f'Состояние спокойствия: {self.state}\n'
              f'Состояние голода: {self.hunger}\n'
              )

    def relax(self):
        print(f'Родитель успокаивает ребёнка {self.name}!')
        if self.state == 'Не спокоен':
            self.state = 'Спокоен'

    def feed(self):
        print(f'Родитель кормит ребёнка {self.name}!')
        if self.hunger == 'Голоден':
            self.hunger = 'Накормлен'


list_kids = ['Monika', 'Sara']
parents_1 = Parents('Alex', 45, list_kids)
parents_1.info()

kids_1 = Child(list_kids[0], 45)
kids_1.kids_info()

kids_2 = Child(list_kids[1], 45)
kids_2.kids_info()

kids_1.relax()
kids_1.kids_info()

kids_2.feed()
kids_2.kids_info()