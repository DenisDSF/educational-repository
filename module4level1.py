def binary_search(sorted_list, search_request, start, stop):
    if stop >= start:
        list_center = (start + stop) // 2
        if sorted_list[list_center] == search_request:
            return list_center
        elif sorted_list[list_center] > search_request:
            return binary_search(sorted_list, search_request,
                                 start, list_center - 1)
        else:
            return binary_search(sorted_list, search_request,
                                 list_center + 1, stop)
    else:
        return False


list_lenght = 70
sorted_list = [(i + 1) * 2 for i in range(list_lenght)]
search_request = 121
list_position = binary_search(sorted_list, search_request,
                              0, len(sorted_list) - 1)
if not list_position:
    print('Число в списке отсутствует!')
else:
    print('Число в списке! Индекс числа в списке: ', list_position)



