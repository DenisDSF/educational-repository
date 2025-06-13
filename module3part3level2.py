def find_words(word_list, max_word_length):
    text = ''
    for i in word_list:
        if len(i) < max_word_length:
            text += i + ' '
    return text


max_word_length = 5
s = '''Было просто пасмурно, дуло с севера
 А к обеду насчитал сто градаций серого.
 Так всегда первого ноль девятого
 Толи весь мир сошёл с ума, толи я - того...
 На столе записка от нее смятая
 Недопитый виски допиваю с матами.
 Посмотрю в окно, допишу главу
 Первое сентября, дворник жжёт листву.
 Серым облакам наплевать на нас
 Если знаешь как жить - живи
 Ты хотела плыть как все - так плыви!'''
s = s.replace(',', '').replace('.', '').replace('!', '').replace('-', '')
word_list = s.split()

print(find_words(word_list, max_word_length))