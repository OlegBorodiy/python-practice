import random


class Home:
    def __init__(self):
        self.food = 50
        self.cash = 0

    def add_food(self, amount):
        self.food += amount
        return self.food

    def take_food(self, amount):
        self.food -= amount
        return self.food

    def add_cash(self, amount):
        self.cash += amount
        return self.cash

    def take_cash(self, amount):
        self.cash -= amount
        return self.cash


class Man:
    def __init__(self, name, home_class):
        self.name = name
        self.state = 50
        self.home_class = home_class

    def is_dead(self):
        if self.state < 0:
            print(f'{self.name} умер от голода..')
            result = 'Dead'
            return result

    def eating(self):
        self.state += 30
        remains_food = self.home_class.take_food(15)
        print(f'{self.name} поел!\nЕго сытость теперь: {self.state}'
              f'\nА вот еды стало: {remains_food}\n')

    def shoping(self):
        remains_food = self.home_class.add_food(30)
        remains_cash = self.home_class.take_cash(20)
        print(f'{self.name} Сходил в магазин за едой!\nЕды теперь: {remains_food}'
              f'\nА вот денег стало: {remains_cash}\n')

    def job(self):
        self.state -= 20
        remains_cash = self.home_class.add_cash(20)
        print(f'{self.name} Поработал!\nДенег теперь: {remains_cash}'
              f'\nА вот сытость стала: {self.state}\n')

    def gaming(self):
        self.state -= 15
        print(f'{self.name} поиграл!\nСытость стала: {self.state}\n')


home = Home()
man_1 = Man('Коля', home)
man_2 = Man('Петя', home)

flag = True

for _ in range(365):
    print('День', str(_ + 1) + '-й')
    for user in [man_1, man_2]:
        random_number = random.randint(1, 6)
        if user.state < 20 and home.food >= 15:
            user.eating()
        else:
            if home.food < 10 and home.cash >= 15:
                user.shoping()
            else:
                if home.cash < 50:
                    user.job()
                else:
                    if random_number == 1:
                        user.job()
                    else:
                        if random_number == 2 and home.food >= 15:
                            user.eating()
                        else:
                            user.gaming()
        if user.is_dead() == 'Dead':
            flag = False
            break
    if not flag:
        break