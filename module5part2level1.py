import json

class Model:

    def some_func(self):
        pass

    def save(self, file_name):
        list1 = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        list2 = list(filter(lambda x: not x.startswith('_'), dir(self)))
        result = list(filter(lambda x: x not in list1, list2))
        data_to_save = {}
        for i in result:
            attr = getattr(self, i)
            data_to_save.update({i: attr})
        saving_file = file_name + '.json'
        with open(saving_file, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False)

    @classmethod
    def restore(cls, data):
        with open(data, 'r', encoding='utf-8') as file:
            reconstruct = json.load(file)
        temp_object = cls()
        [setattr(temp_object, key, val) for key, val in reconstruct.items()
         if hasattr(temp_object, key)]
        return temp_object

class Book(Model):

    def __init__(self, title = None, text = None, author = None):
        self.title = title
        self.text = text
        self.author = author

book1_title = 'Титул'
book1_text_sample = 'Текст'
book1_author = 'Автор'
book_1 = Book(book1_title, book1_text_sample, book1_author)
file_name = input('Введите название сохраняемого файла: ')
book_1.save(file_name)

book_2 = Book.restore('book2.json')
print(book_2.title, book_2.text, book_2.author)
