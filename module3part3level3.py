def make_max_num(num_list):
    num_list_temp = [str(i) for i in num_list]
    num_list_temp = sorted(num_list_temp, reverse=True)
    max_num = ''
    for i in num_list_temp:
        max_num += i
    max_num = int(max_num)
    return max_num


num_list = [75, 4 , 905, 841, 8400, 19, 91]
print('Максимальное число из массива составит:', make_max_num(num_list))