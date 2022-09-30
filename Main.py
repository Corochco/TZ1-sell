from Class import *
import time

def rd(file):
    try:
        f = open(file, encoding="utf8")
        line = f.readline()
        array = []
        while line != '':
            first_sep = line.find(',')
            second_sep = line.rfind(',')
            full_name, email, number = line[:first_sep], line[first_sep + 2:second_sep], line[second_sep + 2:len(line)-1]
            array.append(Contact(full_name, email, number))
            line = f.readline()
        return array
    except FileNotFoundError:
        print('Указано неврное имя файла')
        return [0]
    
    
print('Введите имя файла с бд')
file = input()
file = file + '.txt'
array = rd(file)
while array == [0]:
    print('Введите имя файла с бд')
    file = input()
    file = file + '.txt'
    array = read(file)    
print('Введите команду из списка:')
print('Поиск по номеру телефона')
print('Поиск по адресу электронной почты')
print('Поиск по Фамилии и(или) Имени и(или) Отчеству')
print('Показать все контакты, у которых не заполнен номер телефона')
print('Показать все контакты, у которых не заполнен адрес электронной почты')
print('Завершить')
string = input()
while string != 'завершить':
    if string == 'Поиск по номеру телефона':
        print('Ведите номер телефона или назад, если хотите вернуться')
        line = input()
        if line == 'назад':
            pass
        else:
            counter = 0
            lst = []
            for i in array:
                if line == i.number:
                    lst.append(i)
                    counter += 1
            if counter == 0:
                print('Совпадений не найдено')
            elif counter == 1:
                print('Найдено 1 совпадение:')
                lst[0].prnt()
            else:
                print('Найдено', counter, 'совпадений:')
                for i in lst:
                    i.prnt()
    elif string == 'Поиск по адресу электронной почты':
        print('Ведите адрес электронной почты или назад, если хотите вернуться')
        line = input()
        if line == 'назад':
            pass
        else:
            counter = 0
            lst = []
            for i in array:
                print(i.email)
                if line == i.email:
                    lst.append(i)
                    counter += 1
            if counter == 0:
                print('Совпадений не найдено')
            elif counter == 1:
                print('Найдено 1 совпадение:')
                lst[0].prnt()
            else:
                print('Найдено', counter, 'совпадений:')
                for i in lst:    
                    i.prnt()
    elif string == 'Поиск по Фамилии и(или) Имени и(или) Отчеству':
        print('Введите Фамилию и(или) Имя и(или) Отчество или назад, если хотите вернуться')
        line = input()
        if line == 'назад':
            pass
        else:
            counter = 0
            lst = []
            for i in array:
                if line in i.full_name:
                    lst.append(i)
                    counter += 1
            if counter == 0:
                print('Совпадений не найдено')
            elif counter == 1:
                print('Найдено 1 совпадение:')
                lst[0].prnt()
            else:
                print('Найдено', counter, 'совпадений:')
                for i in lst:
                    i.prnt()
    elif string == 'Показать все контакты, у которых не заполнен номер телефона':
        counter = 0
        lst = []
        for i in array:
            if i.number == '':
                lst.append(i)
                counter += 1
        if counter == 0:
            print('Совпадений не найдено')
        elif counter == 1:
            print('Найдено 1 совпадение:')
            lst[0].prnt()
        else:
            print('Найдено', counter, 'совпадений:')
            for i in lst:
                i.prnt()
    elif string == 'Показать все контакты, у которых не заполнен адрес электронной почты':
        counter = 0
        lst = []
        for i in array:
            if i.email == '':
                lst.append(i)
                counter += 1
        if counter == 0:
            print('Совпадений не найдено')
        elif counter == 1:
            print('Найдено 1 совпадение:')
            lst[0].prnt()
        else:
            print('Найдено', counter, 'совпадений:')
            for i in lst:
                i.prnt()
    elif string == 'Завершить':
        break
    else:
        print('Я не умею выполнять такую команду')
    time.sleep(1)
    print('Введите команду из списка:')
    print('Поиск по номеру телефона')
    print('Поиск по адресу электронной почты')
    print('Поиск по Фамилии и(или) Имени и(или) Отчеству')
    print('Показать все контакты, у которых не заполнен номер телефона')
    print('Показать все контакты, у которых не заполнен адрес электронной почты')
    print('Завершить')    
    string = input()
print('Пока, пока...')
time.sleep(1)