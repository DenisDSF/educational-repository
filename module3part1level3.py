num = input('Введите целое число: ')
if num.isdigit() != True:
    while num.isdigit() != True:
        num = input('Введеные данные не являются целым числом. '
                  'Введите целое число: ')
nums_summ = 0
for i in num:
    nums_summ += int(i)
print('Сумма цифр введенного числа равна',nums_summ)