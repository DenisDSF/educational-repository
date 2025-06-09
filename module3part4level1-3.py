import json
import os


def checking_file_existence(file):
    if os.path.exists(file) != True:
        with open(file, 'w') as f:
            empty_dict = {}
            json.dump(empty_dict, f)


def register(login, password):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
    if login in user_data.keys():
        print('Пользователь с таким логином уже существует.')
    else:
        user_data[login] = password
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)


def logging_in(login, password):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
        if login in user_data.keys() and user_data[login] == password:
            print('Вы вошли!')
            return 'выход'
        else:
            print('Неверный логин или пароль.')


checking_file_existence('user_data.json')
while True:
    user_choice = input('Выберите действие (регистрация/вход/выход): ')
    if user_choice == 'регистрация':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        register(login, password)
    elif user_choice == 'вход':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if logging_in(login, password) == 'выход':
            break
    elif user_choice == 'выход':
        break
    else:
        print('Неверная команда')
