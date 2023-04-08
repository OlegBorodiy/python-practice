import random


class Card:
    rang_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}
    used_cards = list()

    def get_card(self, name):
        card = dict()
        flag = True
        while flag == True:
            card = Deck.generate()
            if card not in Card.used_cards:
                flag = False
        Card.used_cards.append(card)
        key, value = next(iter(card.items()))
        if name != 'Компьютер':
            print(f'Игроком {name} получена карта {key} мастью {value}')
        if key == 'Туз' and (self.rang + 11) > 21:
            self.rang += 1
        else:
            self.rang += Card.rang_dict[key]
        if name != 'Компьютер':
            print(f'Текущий общий ранг: {self.rang}')
        return card


class Deck:
    def generate():
        new_couple = dict()
        four_suits = ['Пик', 'Червей', 'Треф', 'Бубен']
        all_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        new_couple[random.choice(all_value)] = random.choice(four_suits)
        return new_couple.copy()


class Player:
    def __init__(self, name):
        self.name = name
        self.rang = 0
        Card.get_card(self, self.name)
        Card.get_card(self, self.name)

    def get_new_card(self):
        Card.get_card(self, self.name)


Player_1 = Player('Игорь')
Player_2 = Player('Компьютер')

answer = 1
while answer == 1 and Player_1.rang < 21:
    answer = int(input('\nВзять карту или остановиться?\n1 - взять\n2 - остановиться\n'))
    if answer == 1:
        Player_1.get_new_card()
    if Player_2.rang < 16:
        Player_2.get_new_card()


if (Player_1.rang > Player_2.rang and Player_1.rang <= 21) \
        or (Player_2.rang > 21 and Player_1.rang < 21) \
        or (Player_1.rang > 21 and Player_2.rang > 21 and Player_1.rang < Player_2.rang):
    print(f'Вы победили компьютер! У Вас {Player_1.rang} очков, а у компьютера {Player_2.rang}!')
elif (Player_2.rang > Player_1.rang and Player_2.rang <= 21) \
        or (Player_1.rang > 21 and Player_2.rang < 21) \
        or (Player_1.rang > 21 and Player_2.rang > 21 and Player_2.rang < Player_1.rang):
    print(f'Вы проиграли компьютеру! У Вас {Player_1.rang} очков, а у компьютера {Player_2.rang}!')
else:
    print(f'Ничья! У Вас {Player_1.rang} очков, а у компьютера {Player_2.rang}!')

