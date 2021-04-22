from random import *
kasutajanimed = []
paroolid = []

def kasutajaandmed():
    log = input('Введи имя пользователя ')
    password = input('Введи пароль ')
    return log, password

def login(kasutajanimed,log,password):
    n = len(kasutajanimed)
    signal = 0
    for i in range(n):
        if kasutajanimed[i] == log and paroolid[i] == password:
            print("Авторизация прошла успешно. Вы зашли в систему")
            signal = 1
        elif kasutajanimed[i] == log and paroolid[i] != password:
            print("Неверный пароль")
            signal = -1
    if signal == 0:      
        print("Вы - новый пользователь")
        reg = input("Желаете ли зарегистрироваться? y/n ")
        if reg == 'n':
            print("Вы не сможете пользоваться системой")
        elif reg == 'y':
            print("Начнём процесс регистрации")
            registratsija(log,password,kasutajanimed,paroolid)
        else:
            print("Ошибка ввода")
    
def registratsija(log,password,kasutajanimed,paroolid):
    kasutajanimed.append(log)
    print("Вы - новый пользователь")
    print("Сейчас будем создавать новый пароль")
    valik = input("Создаём пароль: a - автоматически, m - вручную: ")
    if valik == 'a':
        new_password = automat_parol()
        paroolid.append(new_password)
        print(kasutajanimed)
        print(paroolid)
    elif valik == 'm':
        new_password = input("Введите пароль (мин. 12 символов) ")
        n = len(new_password)
        while n < 12:
            new_password = input('Слишком короткий пароль. Введите ещё раз ')
            n = len(new_password)
        paroolid.append(new_password)
    else:
        print("Ошибка ввода")

    
def automat_parol():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    shuffle(ls)
    psword = ''.join([choice(ls) for x in range(12)])
    return psword     

while True:
    print()
    print("Пройти регистрацию - r")
    print("Авторизироваться - l")
    print("Закончить работу - x")
    valik = input("Сделайте свой выбор ")
    if valik == 'r':
        log, password = kasutajaandmed()
        registratsija(log,password,kasutajanimed,paroolid)
    elif valik == 'l':
        log, password = kasutajaandmed()
        login(kasutajanimed,log,password)
    elif valik == 'x':
        print("Завершение работы")
        break
    else:
        print("Ошибка ввода")

