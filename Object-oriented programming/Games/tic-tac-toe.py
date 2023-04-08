import random

class Board:
    board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    def print_current_state():
        print('Текущее состояние поля (ячейки с цифрами свободны):')
        print("+---+---+---+")
        print(f"| {Board.board[1]} | {Board.board[2]} | {Board.board[3]} |")
        print("+---+---+---+")
        print(f"| {Board.board[4]} | {Board.board[5]} | {Board.board[6]} |")
        print("+---+---+---+")
        print(f"| {Board.board[7]} | {Board.board[8]} | {Board.board[9]} |")
        print("+---+---+---+")
    def check_win():
        if Board.board[1] == Board.board[2] == Board.board[3] \
                or Board.board[1] == Board.board[4] == Board.board[7] \
                or Board.board[1] == Board.board[5] == Board.board[9] \
                or Board.board[2] == Board.board[5] == Board.board[8] \
                or Board.board[3] == Board.board[6] == Board.board[9] \
                or Board.board[3] == Board.board[5] == Board.board[7] \
                or Board.board[4] == Board.board[5] == Board.board[6] \
                or Board.board[7] == Board.board[8] == Board.board[9]:
            print('Победа!')
            Board.print_current_state()
            return 'Конец!'


class Player():
    def __init__(self, name):
        self.name = name
    def choice_cell(self, symbol):
        while True:
            choice = int(input('Введите свободный номер клетки: '))
            if Board.board[choice] != 'X' and Board.board[choice] != 'O':
                Board.board[choice] = symbol
                break
            else:
                print('Данная клетка уже занята! Выберете новую!')


player_1 = Player('Настя')
player_2 = Player('Олег')

random_choice = random.randint(1, 2)

if random_choice == 1:
    first_player = player_1
    second_player = player_2
    print(f'Первым ходит {first_player.name} - этому игроку выпало ставить крестики!')
else:
    first_player = player_2
    second_player = player_1
    print(f'Первым ходит {first_player.name} - этому игроку выпало ставить крестики!')

while True:
    print(f'\nХод игрока {first_player.name}!')
    Board.print_current_state()
    first_player.choice_cell('X')
    check = Board.check_win()
    if check == 'Конец!':
        break
    print(f'\nХод игрока {second_player.name}!')
    Board.print_current_state()
    second_player.choice_cell('O')
    if check == 'Конец!':
        break

print('Игра завершена!')
