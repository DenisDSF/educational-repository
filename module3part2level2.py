from random import randint


def find_max(matrix):
    max_num = 0
    for i in matrix:
        for x in i:
            if max_num < x:
                max_num = x
    return max_num


num = 5
matrix = [[randint(0, 100) for i in range(num)] for j in range(num)]
print('Сгенерированная матрица:')
for i in matrix:
    print(i)
print('Максимальный элемент сгенерированной матрицы: ', find_max(matrix))