def checking_digits(x):
    if x.isdigit():
        return True
    else:
        return False


num = input('Введите целое число: ')
while checking_digits(num) != True:
    num = input('Введеные данные не являются целым числом. '
              'Введите целое число: ')
nums_summ = 0
for i in num:
    nums_summ += int(i)
print('Сумма цифр введенного числа равна',nums_summ)