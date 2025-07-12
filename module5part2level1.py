import json

class Model:

    def some_func(self):
        pass

    def save(self):
        list1 = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        list2 = list(filter(lambda x: not x.startswith('_'), dir(self)))
        result = list(filter(lambda x: x not in list1, list2))
        data_to_save = {}
        for i in result:
            attr = getattr(self, i)
            data_to_save.update({i: attr})
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False)


class Book(Model):

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

book1_title = 'Титул'
book1_text_sample = 'Текст'
book1_author = 'Автор'
book_1 = Book(book1_title, book1_text_sample, book1_author)
book_1.save()