x1 = float(input('Введите первое число: '))
x2 = float(input('Введите второе число: '))
max_num = (x1 > x2) * x1 + (x2 >= x1) * x2
print('Наибольшее число:', max_num)