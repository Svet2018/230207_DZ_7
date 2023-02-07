def dict_print(dat): #Выводит меню на экран
    print()
    print('Меню программы:')
    print('*'*25)
    for key, value in dat.items():
        print(key, value)
    print()


def menu(num): #Действие с меню
    match num:
        case '1':
            print('Автобусный парк: ')
            print('-'*35)
            print_func('bus.txt')
        case '2':
            print('-' * 35)
            add_bus('bus.txt')
        case '3':
            print('Водители автобусов: ')
            print('-' * 35)
            print_func('driver.txt')
        case '4':
            print('-' * 35)
            add_driver('driver.txt')
        case '5':
            print('Маршруты автобусов: ')
            print('-' * 35)
            print_func('travel.txt')
        case '6':
            print('-' * 35)
            add_travel('travel.txt')
        case '7':
            print('Вы вышли из программы.')
            print('-' * 35)
            exit()
        case _:
            print(f'Выбрано другое действие')
            print('-' * 35)


def print_func(file_name):  #Показывает записи из указанных текстовых файлов.
    with open(file_name, 'r') as data:
        new_str = data.read()
        answer = ''
        for i in range(len(new_str) - 1):
            if new_str[i] != ',':
                answer += new_str[i]
        print(answer)


def add_bus(file_name):#Добавление автобуса
    print(f'Чтобы добавить автобус.')
    bus_id = input(f'Введите ID автобуса в формате "bus_N": ').lower()
    bus_num = input(f'Введите номер: ').upper()
    bus_mark = input(f'Введите марку: ').capitalize()
    bus_year = input(f'Введите год выпуска: ')
    bus_travel = input(f'Введите пробег: ')
    new_data = [bus_id, bus_num, bus_mark, bus_year, bus_travel]
    new_str = '\n' + ', '.join(new_data) + ','
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(new_str)
    print(f'Автобус добавлен в базу данных.')


def add_driver(file_name):#Добавление водителя
    print(f'Чтобы добавить водителя.')
    person_id = input(f'Введите ID водителя в формате driver_N: ').lower()
    person_surname = input(f'Введите фимилию: ').capitalize()
    person_name = input(f'Введите имя: ').capitalize()
    person_patronymic = input(f'Введите отчество: ').capitalize()
    person_telephone = input(f'Введите год рождения: ')
    new_data = [person_id, person_surname, person_name, person_patronymic, person_telephone]
    new_str = '\n' + ', '.join(new_data) + ','
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(new_str)
    print(f'Водитель добавлен в базу данных.')


def add_travel(file_name):#Добавление маршрута
    print(f'Чтобы добавить маршрут.')
    travel_id = input(f'Введите ID маршрута в формате "travel_N": ').lower()
    travel_name = input(f'Введите название маршрута: ').capitalize()
    travel_num = input(f'Введите номер маршрута: ')
    bus_id = input(f'Введите  ID автобуса: ')
    person_id = input(f'Введите ID водителя: ')
    new_data = [travel_id, travel_name, travel_num, bus_id, person_id]
    new_str = '\n' + ', '.join(new_data) + ','
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(new_str)
    print(f'Маршрут добавлен в базу данных.')
    
  
