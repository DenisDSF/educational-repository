class StringVar:

    def __init__(self, text):
        self.text = text

    def set(self, letter):
        return self.text.replace(letter, letter.upper())

    def get(self):
        return self.text


test_text = 'Карл у Клары украл кораллы, а Клара у Карла украла кларнет.'
lower_letter_in_text = 'а'
tongue_twister = StringVar(test_text)
print(f'Содержимое строки: \n{tongue_twister.get()}')
print(f'Вот текст со всеми буквами "{lower_letter_in_text}" в верхнем '
      f'регистре:\n{tongue_twister.set(lower_letter_in_text)}')