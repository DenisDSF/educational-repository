from __future__ import annotations
import sqlite3
from abc import ABC, abstractmethod


#Класс, работающий с базой данных.
class DBConnector(ABC):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(
                cls,
                *args,
                **kwargs
            )
        return cls.instance

    @abstractmethod
    def connect(self, database: str):
        raise NotImplementedError

    @abstractmethod
    def close_connection(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self, query: str):
        raise NotImplementedError

    @abstractmethod
    def execute_many(self, query: str, seq_of_parameters: list):
        raise NotImplementedError

    @abstractmethod
    def fetch(self, query: str) -> list:
        raise NotImplementedError


#Класс получает классы, объекты, параметры от менеджера.
#Обрабатывает и возвращает список списков с параметрами для создания запросов.
class DBQueryListCreator(ABC):
    @abstractmethod
    def create_table_query_list(class_name) -> list[lists]:
        raise NotImplementedError

    @abstractmethod
    def create_insert_query_list(obj) -> list[lists]:
        raise NotImplementedError

    @abstractmethod
    def create_insert_many_query_list(obj_tuple) -> list[lists]:
        raise NotImplementedError

    @abstractmethod
    def create_find_query_list(parameters_dict) -> list[lists]:
        raise NotImplementedError


#Класс создающий запрос на создание таблицы.
#Получает список списков с параметрами от менеджера.
#Возвращает готовый для передачи коннектору запрос.
class DBCreateTableQuery(ABC):
    @abstractmethod
    def create_table_query(table_name: str,
                           fields: [lists]) -> query:
        raise NotImplementedError


#Класс создающий запросы на внесение строк в таблицы.
#Получает список списков с параметрами от менеджера.
#Возвращает готовый для передачи коннектору запрос.
class DBCreateRowQuery(ABC):
    @abstractmethod
    def create_one_row_query(table_name: str, row_data: list[lists]) -> query:
        raise NotImplementedError

    @abstractmethod
    def create_many_row_data(table_name: str, rows_data: list[lists]) \
            -> [query, seq_of_parameters]:
        raise NotImplementedError


#Класс создающий запросы на поиск информации в таблицах.
#Получает список списков с параметрами от менеджера.
#Возвращает готовый для передачи коннектору запрос.
class DBInfoFindQuery(ABC):
    @abstractmethod
    def create_find_info_query(finding_list: list[lists]) -> query:
        raise NotImplementedError


#Класс находящий связанные столбцы таблиц.
#Получает от DBQueryListCreator список с названиями классов.
#Обрабатывает и возвращает список со связанными столбцами.
class DBConnectionFinder(ABC):
    @abstractmethod
    def find_connection(obj_list) -> list:
        raise NotImplementedError


#Класс типов данных колонок таблиц.
class Field(ABC):
    @abstractmethod
    def to_database_type(self) -> str:
        raise NotImplementedError


#Класс заменяющий атрибуты таблиц на атрибуты объектов в таблицах.
class Model(ABC):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


#Класс обрабатывающий запросы пользователя.
class DBManager(ABC):
    @abstractmethod
    def create_table(self, class_name):
        raise NotImplementedError

    @abstractmethod
    def add(self, object):
        raise NotImplementedError

    @abstractmethod
    def add_many(self, *objects):
        raise NotImplementedError

    @abstractmethod
    def select(
            self,
            class_name,
            join=None,
            column_names=None,
            filtering_conditions=None
    ):
        raise NotImplementedError


class SQliteConnector(DBConnector):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQliteConnector, cls).__new__(
                cls,
                *args,
                **kwargs
            )
        return cls.instance

    def connect(self, database: str):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, query: str):
        self.cursor.execute(query)

    def execute_many(self, query: str, seq_of_parameters: list):
        self.cursor.executemany(query, seq_of_parameters)

    def fetch(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()


class ConnectionFinder(DBConnectionFinder):
    def find_connection(obj_list) -> list:
        obj_name_list = [i.__name__ for i in obj_list]
        connections = []
        for i in obj_list:
            for key, value in vars(i).items():
                if (isinstance(value, ForeignKey)
                        and value.__dict__['parent_table_name']
                        in obj_name_list):
                    connection_self = i.__name__ + '.' + key
                    connection_with = value.parent
                    connection = connection_self + ' = ' + connection_with
                    connections.append(connection)
        return connections


class QueryListCreator(DBQueryListCreator):
    def create_table_query_list(class_name) -> list[lists]:
        table_fields_list = []
        foreign_key_list =[]
        for key, value in class_name.__dict__.items():
            temp_list = [None, None]
            foreign_key_temp_list =[None, None]
            if key.startswith('_'):
                continue
            temp_list[0] = key
            temp_list[1] = value.to_database_type()
            table_fields_list.append(temp_list)
            if isinstance(value, ForeignKey):
                foreign_key_temp_list[0] = 'FOREIGN KEY'
                foreign_key_temp_list[1] = value.to_database_foreign_key()
                foreign_key_list.append(foreign_key_temp_list)
        table_fields_list += foreign_key_list
        return table_fields_list

    def create_insert_query_list(obj) -> list[lists]:
        row_fields_list = []
        for key, value in obj.__dict__.items():
            temp_list = [None, None]
            temp_list[0] = key
            temp_list[1] = value
            row_fields_list.append(temp_list)
        return row_fields_list

    def create_insert_many_query_list(obj_tuple) -> list[lists]:
        rows_fields_list = []
        for i in obj_tuple:
            temp_fields_list = []
            for key, value in i.__dict__.items():
                temp_list = [None, None]
                temp_list[0] = key
                temp_list[1] = value
                temp_fields_list.append(temp_list)
            rows_fields_list.append(temp_fields_list)
        return rows_fields_list

    def create_find_query_list(parameters_dict) -> list[lists]:
        class_names_list = [parameters_dict['class_name'].__name__]
        filtering_condition = []
        connections = []
        if parameters_dict['join'] is not None:
            join_classes = []
            if type(parameters_dict['join']) != type(tuple()):
                class_names_list.append(parameters_dict['join'].__name__)
                join_classes.append(parameters_dict['join'])
            else:
                for i in parameters_dict['join']:
                    class_names_list.append(i.__name__)
                    join_classes.append(i)
            classes = [parameters_dict['class_name']] + join_classes
            connections = ConnectionFinder.find_connection(classes)

        if (parameters_dict['column_names'] is not None
                and type(parameters_dict['column_names']) == type(tuple())):
            column_names_list = []
            for i in parameters_dict['column_names']:
                for j in Model.__subclasses__():
                    for k, v in vars(j).items():
                        if v == i:
                            name = j.__name__ + '.' + k
                            column_names_list.append(name)
                            break
        elif parameters_dict['column_names'] is not None:
            for i in Model.__subclasses__():
                for k, v in vars(i).items():
                    if v == parameters_dict['column_names']:
                        name = i.__name__ + '.' + k
                        column_names_list = [name]
                        break
        else:
            column_names_list = ['*']

        if (parameters_dict['filtering_conditions'] is not None
                and type(parameters_dict['filtering_conditions'])
                == type(tuple())):
            filtering_condition = [i for i
                                   in parameters_dict['filtering_conditions']]
        elif parameters_dict['filtering_conditions'] is not None:
            filtering_condition = [parameters_dict['filtering_conditions']]

        finding_list = ([class_names_list]
                        + [column_names_list]
                        + [filtering_condition]
                        + [connections])
        return finding_list


class TableQueryCreator(DBCreateTableQuery):
    def create_table_query(table_name: str,
                           fields: list[lists]) -> query:
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        for i in fields:
            if i[0] != 'FOREIGN KEY':
                query += f'{i[0]} {i[1]}, '
            else:
                query += f'{i[1]}, '
        query = query[:-2] + ')'
        return query


class InfoInserter(DBCreateRowQuery):
    def create_one_row_query(table_name: str, row_data: list[lists]) -> query:
        field_names = f'INSERT INTO {table_name} ('
        values = f'VALUES ('
        for i in row_data:
            field_names += f'{i[0]}, '
            if type(i[1]) != type(str()):
                values += f'{i[1]}, '
            else:
                values += f'"{i[1]}", '
        field_names = field_names[:-2] + ')'
        values = values[:-2] + ')'
        query = field_names + ' ' + values
        return query

    def create_many_row_data(table_name: str, rows_data: list[lists])\
            -> list(query, seq_of_parameters):
        fields_names_list = []
        seq_of_parameters = []
        for i in rows_data:
            temp_list = []
            for j in i:
                if j[0] not in fields_names_list:
                    fields_names_list.append(j[0])
                temp_list.append(j[1])
            seq_of_parameters.append(tuple(temp_list))
        field_names = f'INSERT INTO {table_name} ('
        values = 'VALUES ('
        for i in fields_names_list:
            field_names += f'{i}, '
            values += '?, '
        field_names = field_names[:-2] + ')'
        values = values[:-2] +')'
        query = field_names + ' ' + values
        return [query, seq_of_parameters]


class InfoFinder(DBInfoFindQuery):
    def create_find_info_query(finding_list: list[lists]) -> query:
        table_names = ''
        connection = ''
        filtering_conditions = ''
        for i in finding_list[0]:
            table_names += i + ', '
        table_names = table_names[:-2]
        column_names = ''
        for i in finding_list[1]:
            column_names += i + ', '
        column_names = column_names[:-2]
        query = f'SELECT {column_names} FROM {table_names}'
        if len(finding_list[0]) > 1:
            for i in finding_list[3]:
                connection += i + ' AND '
            connection = connection[:-5]
        if len(finding_list[2]) > 0:
            for i in finding_list[2]:
                filtering_conditions += i + ' AND '
            filtering_conditions = filtering_conditions[:-5]
        if connection != '':
            query += ' WHERE ' + connection
        if connection != '' and filtering_conditions != '':
            query += ' AND ' + filtering_conditions
        elif connection == '' and filtering_conditions !='':
            query += ' WHERE ' + filtering_conditions
        return query


class ForeignKey(Field):
    def __init__(
            self,
            parent_table_name,
            parent_table_field_name,
            primary_key=False):
        self.parent_table_name = parent_table_name
        self.parent_table_field_name = parent_table_field_name
        self.parent = (self.parent_table_name
                       + '.'
                       + self.parent_table_field_name)
        self.field_type = eval(self.parent)
        if isinstance(self.field_type, IntegerField):
            if primary_key:
                self.field_type = IntegerField(primary_key=True)
            else:
                self.field_type = IntegerField()

    def to_database_type(self) -> str:
        return self.field_type.to_database_type()

    def to_database_foreign_key(self) -> str:
        self.name = None
        for i in Model.__subclasses__():
            for k, v in vars(i).items():
                if v == self:
                    self.name = k
                    break
        return (f'FOREIGN KEY ({self.name}) '
                f'REFERENCES {self.parent_table_name} '
                f'({self.parent_table_field_name})')


class IntegerField(Field):
    def __init__(self, primary_key=False):
        self.primary_key = primary_key

    def to_database_type(self) -> str:
        if self.primary_key:
            return 'INTEGER PRIMARY KEY'
        return 'INTEGER'


class CharField(Field):
    def __init__(self, length=32):
        self.length = length

    def to_database_type(self) -> str:
        return f'VARCHAR({self.length})'


class Manager(DBManager):
    def __init__(self, database_file_name: str):
        self.database_file_name = database_file_name
        self.connector = SQliteConnector
        self.query_list_creator = QueryListCreator
        self.table_query_creator = TableQueryCreator
        self.info_inserter = InfoInserter
        self.info_finder = InfoFinder

    def create_table(self, class_name):
        list_for_query = (self.query_list_creator.
                          create_table_query_list(class_name))
        query = (self.table_query_creator.
                 create_table_query(class_name.__name__, list_for_query))
        self.connector.connect(self, self.database_file_name)
        self.connector.execute(self, query)
        self.connector.commit(self)
        self.connector.close_connection(self)

    def add(self, object):
        list_for_query = (self.query_list_creator.
                          create_insert_query_list(object))
        query = (self.info_inserter.
                 create_one_row_query(object.__class__.__name__, list_for_query))
        self.connector.connect(self, self.database_file_name)
        self.connector.execute(self, query)
        self.connector.commit(self)
        self.connector.close_connection(self)

    def add_many(self, *objects):
        list_for_list_creator = (self.query_list_creator.
                                 create_insert_many_query_list(objects))
        table_name = objects[0].__class__.__name__
        rows_data = (self.info_inserter.
                     create_many_row_data(table_name, list_for_list_creator))
        query = rows_data[0]
        seq_of_parameters = rows_data[1]
        self.connector.connect(self, self.database_file_name)
        self.connector.execute_many(self, query, seq_of_parameters)
        self.connector.commit(self)
        self.connector.close_connection(self)

    def select(
            self,
            class_name,
            join=None,
            column_names=None,
            filtering_conditions=None
    ):
        parameters_dict = {
            'class_name': class_name,
            'join': join,
            'column_names': column_names,
            'filtering_conditions': filtering_conditions
        }
        list_for_finding = self.query_list_creator.create_find_query_list(parameters_dict)
        query = self.info_finder.create_find_info_query(list_for_finding)
        self.connector.connect(self, self.database_file_name)
        result = self.connector.fetch(self, query)
        self.connector.close_connection(self)
        return result


class Students(Model):
    id_field = IntegerField(primary_key=True)
    name = CharField(32)
    surname = CharField(32)
    age = IntegerField()
    city = CharField(32)


class Courses(Model):
    id_field = IntegerField(primary_key=True)
    name = CharField(32)
    time_start = CharField(32)
    time_end = CharField(32)


class StudentCourses(Model):
    student_id = ForeignKey(
        'Students',
        'id_field',
        primary_key=True
    )
    course_id = ForeignKey(
        'Courses',
        'id_field'
    )


manager = Manager('db1.sqlite')
manager.create_table(Students)

max_brooks = Students(
    id_field=1,
    name='Max',
    surname='Brooks',
    age=24,
    city='Spb'
)
john_stones = Students(
    id_field=2,
    name='John',
    surname='Stones',
    age=15,
    city='Spb'
)
andy_wings = Students(
    id_field=3,
    name='Andy',
    surname='Wings',
    age=45,
    city='Manchester'
)
kate_brooks = Students(
    id_field=4,
    name='Kate',
    surname='Brooks',
    age=34,
    city='Spb'
)
manager.add(max_brooks)
manager.add_many(john_stones, andy_wings, kate_brooks)

manager.create_table(Courses)
python_course = Courses(
    id_field=1,
    name='Python',
    time_start='21.07.21',
    time_end='21.08.21')
java_course = Courses(
    id_field=2,
    name='Java',
    time_start='13.07.21',
    time_end='16.08.21'
)
manager.add_many(python_course, java_course)

manager.create_table(StudentCourses)
max_brooks_course = StudentCourses(
    student_id=1,
    course_id=1
)
john_stones_course = StudentCourses(
    student_id=2,
    course_id=1
)
andy_wings_course = StudentCourses(
    student_id=3,
    course_id=1
)
kate_brooks_course = StudentCourses(
    student_id=4,
    course_id=2
)
manager.add_many(max_brooks_course, john_stones_course, andy_wings_course, kate_brooks_course)

print(manager.select(Students))
print(manager.select(Students, filtering_conditions='age > 30'))
print(manager.select(
    Students,
    column_names=(Students.name, Students.surname),
    filtering_conditions='age > 30'
))
print(manager.select(
    Students,
    join=(StudentCourses, Courses),
    column_names=(Students.name, Students.surname),
    filtering_conditions='Courses.name = "Python"'
))
print(manager.select(
    Students,
    join=(StudentCourses, Courses),
    column_names=(Students.name, Students.surname),
    filtering_conditions=('city = "Spb"', 'Courses.name = "Python"')
))


