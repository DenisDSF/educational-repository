import json
import os


def checking_file_existence(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            empty_dict = {}
            json.dump(empty_dict, f)


def register(login, password):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
    if login in user_data.keys():
        return False
    else:
        user_data[login] = password
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)


def logging_in(login, password):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
        if login in user_data.keys() and user_data[login] == password:
            return True
        else:
            return False


checking_file_existence('user_data.json')
while True:
    user_choice = input('Выберите действие (регистрация/вход/выход): ')
    if user_choice == 'регистрация':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if register(login, password) == False:
            print('Пользователь с таким логином уже существует.')
    elif user_choice == 'вход':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if logging_in(login, password) == True:
            print('Вы вошли!')
            break
        else:
            print('Неверный логин или пароль.')
    elif user_choice == 'выход':
        break
    else:
        print('Неверная команда')
