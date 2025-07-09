class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move_point(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


x = 5
y = -6
point1 = Point(x, y)
dx = int(input('Введите расстояние по оси X для перемещения точки: '))
dy = int(input('Введите расстояние по оси Y для перемещения точки: '))
point1.move_point(dx, dy)
print(f'Текущее положение точки по оси X: {point1.get_x()}\n'
      f'Текущее положение точки по оси Y: {point1.get_y()}\n'
      f'Расстояние от центра оси координат до точки: {point1.get_distance()}')

