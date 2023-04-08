class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def x_y_r_return(self):
        return self.x, self.y, self.r

    def square(self):
        return 3.14 * self.r ** 2

    def perimetr(self):
        return 2 * 3.14 * self.r

    def enlarge(self):
        amount = int(input('\nВо сколько раз увеличить? '))
        self.r *= amount
        print(f'Теперь радиус равен {self.r}!\n')

    def compare(cir_1, cir_2):
        d = (((abs(cir_1[0]) + abs(cir_2[0])) ** 2) + ((abs(cir_1[1]) + abs(cir_2[1])) ** 2)) ** 0.5
        if abs(cir_1[2]) + abs(cir_2[2]) > d \
                and abs(cir_1[2]) + d > abs(cir_2[2]) \
                and abs(cir_2[2]) + d > abs(cir_1[2]):
            return '\nТреугольники пересекаются!'
        else:
            return '\nТреугольники НЕ пересекаются!'


circle_1 = Circle(1, 3, 4)
circle_2 = Circle(1, 2, 3)

print(f'Площадь круга: {circle_1.square()}')
print(f'Площадь периметра: {circle_1.perimetr()}')

circle_1.enlarge()
print(f'Площадь круга: {circle_1.square()}')
print(f'Площадь периметра: {circle_1.perimetr()}')
circle_1_x_y_r = circle_1.x_y_r_return()
circle_2_x_y_r = circle_2.x_y_r_return()

print(Circle.compare(circle_1_x_y_r, circle_2_x_y_r))