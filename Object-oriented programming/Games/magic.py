class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Wind:
    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:
    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Wind):
            return Lightning()
        else:
            return None


class Earth:
    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Wind):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    def __str__(self):
        return "Шторм"


class Steam:
    def __str__(self):
        return "Пар"


class Dirt:
    def __str__(self):
        return "Грязь"


class Lightning:
    def __str__(self):
        return "Молния"


class Dust:
    def __str__(self):
        return "Пыль"


class Lava:
    def __str__(self):
        return "Лава"


water = Water()
earth = Earth()
result = water + earth

print(f'При соединении {water} и {earth} получается {result}')