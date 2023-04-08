import random


class Warrior:
    def __init__(self):
        self.health = 100

    def defence(self):
        self.health -= 20


warrior_1 = Warrior()
warrior_2 = Warrior()

while warrior_1.health and warrior_2.health > 0:
    choice = random.randint(1, 2)
    if choice == 1:
        print('Воин №1 наносит урон Воину №2!')
        warrior_2.defence()
        print('У воина №2 осталось {} здоровья\n'.format(warrior_2.health))
    else:
        print('Воин №2 наносит урон Воину №1!')
        warrior_1.defence()
        print('У воина №1 осталось {} здоровья\n'.format(warrior_1.health))
if warrior_1.health == 0:
    print('Одержал победу воин №2!')
else:
    print('Одержал победу воин №1!')



