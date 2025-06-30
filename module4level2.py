import random

def insertion_sort(unsorted_list):
    temp_list = []
    temp_list += unsorted_list
    for i in range(len(temp_list)):
        j = i - 1
        temp_variable = temp_list[i]
        while temp_variable < temp_list[j] and j >= 0:
            temp_list[j + 1] = temp_list[j]
            j -= 1
        temp_list[j + 1] = temp_variable
    return temp_list


list_length = 30
random_list = [random.randint(-100, 100) for i in range(list_length)]
print(f'Случайно сгенерированный массив: \n{random_list}')
print(f'Отсортированный сгенерированный массив: \n{insertion_sort(random_list)}')