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

    def get_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5


point1_x = 5
point1_y = 6
point2_x = -12
point2_y = 8
origin = Point(0, 0)
point1 = Point(point1_x, point1_y)
point2 = Point(point2_x, point2_y)
print(f'Текущее положение первой точки по оси X: {point1.get_x()}\n'
      f'Текущее положение первой точки по оси Y: {point1.get_y()}')
dx = int(input('Введите расстояние по оси X для перемещения первой точки: '))
dy = int(input('Введите расстояние по оси Y для перемещения первой точки: '))
point1.move_point(dx, dy)
print(f'Текущее положение первой точки по оси X: {point1.get_x()}\n'
      f'Текущее положение первой точки по оси Y: {point1.get_y()}\n'
      f'Расстояние от центра оси координат до первой точки: '
      f'{point1.get_distance(origin)}\n')
print(f'Текущее положение второй точки по оси X: {point2.get_x()}\n'
      f'Текущее положение второй точки по оси Y: {point2.get_y()}')
dx = int(input('Введите расстояние по оси X для перемещения второй точки: '))
dy = int(input('Введите расстояние по оси Y для перемещения второй точки: '))
point2.move_point(dx, dy)
print(f'Текущее положение второй точки по оси X: {point2.get_x()}\n'
      f'Текущее положение второй точки по оси Y: {point2.get_y()}\n'
      f'Расстояние от центра оси координат до второй точки: '
      f'{point2.get_distance(origin)}\n')
print(f'Расстояние между первой и второй точками: '
      f'{point1.get_distance(point2)}')


