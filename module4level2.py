import random

def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        j = i - 1
        temp_variable = unsorted_list[i]
        while temp_variable < unsorted_list[j] and j >= 0:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = temp_variable
    return unsorted_list


list_length = 30
random_list = [random.randint(-100, 100) for i in range(list_length)]
print(f'Случайно сгенерированный массив: \n{random_list}')
print(f'Отсортированный сгенерированный массив: \n{insertion_sort(random_list)}')