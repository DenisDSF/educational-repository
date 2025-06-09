def make_max_num(num_list):
    num_list_temp = []
    max_num = ''
    for i in num_list:
        i_str = str(i)
        if len(i_str) > 1:
            after_decimal = '.' + str(len(i_str) - 1) + 'f'
            i =  f'{i / (10 ** (len(i_str) - 1)):{after_decimal}}'
        else:
            i = str(i)
        num_list_temp.append(i)
    num_list_temp.sort()
    num_list_temp.reverse()
    for i in num_list_temp:
        max_num += i
    max_num = max_num.replace('.', '')
    max_num = int(max_num)
    return max_num


num_list = [75, 4 , 9, 841, 8400, 19]
print('Максимальное число из массива составит:', make_max_num(num_list))