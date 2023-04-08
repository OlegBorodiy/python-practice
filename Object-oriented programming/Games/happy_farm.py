class Gardener:
    def __init__(self, count):
        self.name = 'Paolo'
        self.pot_list = [Potatoes(index) for index in range(1, count + 1)]
        self.sum_potatoes = 0
        self.flag = True
        print('Создан новый сад с садовником {}!\n'.format(self.name))

    def all_grow(self):
        print('Картошка прорастает!')
        for i_potatoes in self.pot_list:
            i_potatoes.grow()

    def are_all_ripe(self):
        if not all([i_potatoes.is_ripe() for i_potatoes in self.pot_list]):
            print('Картошка ещё не созрела!\n')
        else:
            self.sum_potatoes += 5
            print('Вся картошка созрела. Собрано {} картошек!\n'.format(self.sum_potatoes))
            self.flag = False


class Potatoes:
    stady_dict = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.stady = 0

    def print_stady(self):
        print('Картошка {} сейчас {}'.format(self.index, Potatoes.stady_dict[self.stady]))

    def grow(self):
        if self.stady < 3:
            self.stady += 1
        self.print_stady()

    def is_ripe(self):
        if self.stady == 3:
            self.stady = 0
            return True
        return False


new_garden = Gardener(5)

for _ in range(6):
    while new_garden.flag is True:
        new_garden.all_grow()
        new_garden.are_all_ripe()

new_garden = Gardener(5)

for _ in range(4):
    while new_garden.flag is True:
        new_garden.all_grow()
        new_garden.are_all_ripe()