def get_annual_amount(bank_deposit, interest_rate):
    annual_amount = bank_deposit * (1 + interest_rate / 100)
    return annual_amount


bank_deposit = int(input('Введите сумму вклада: '))
interest_rate = float(input('Введите процентную ставку вклада: '))
expected_amount = int(input('Введите желаемую сумму на вкладе: '))
deposit_duration = 0

while bank_deposit < expected_amount:
    bank_deposit = int(get_annual_amount(bank_deposit, interest_rate))
    deposit_duration += 1
print('Требуемая продолжительность вклада для достижения желаемой суммы:',
      deposit_duration, 'лет. Сумма на счету составит:', bank_deposit)