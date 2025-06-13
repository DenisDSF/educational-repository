def checking_digits(x):
    while x.isdigit() != True:
        x = input('Введеные данные не являются целым числом. '
                  'Введите целое число: ')
    return x


num = input('Введите целое число: ')
if num.isdigit() != True:
    num = checking_digits(num)
nums_summ = 0
for i in num:
    nums_summ += int(i)
print('Сумма цифр введенного числа равна',nums_summ)