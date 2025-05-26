password = str(input('Введите пароль. Длина пароля должна быть не менее 8 символов. Пароль должен содержать прописные и заглавные буквы: '))
length = len(password)

while length < 8 or password.islower() == True or password.isupper() == True or password.isalpha() != True:
    password = str(input('Длина пароля должна быть не менее 8 символов. Пароль должен содержать прописные и заглавные буквы: '))
    length = len(password)
else:
    print('Введен допустимый пароль')