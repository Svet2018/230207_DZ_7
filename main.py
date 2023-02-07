from func import dict_print
from func import menu


data = {
    1: ' - Вывод автобусов',
    2: ' - Добавление автобусов',
    3: ' - Вывод водителей',
    4: ' - Добавление водителей',
    5: ' - Вывод маршрута',
    6: ' - Добавление маршрута',
    7: ' - Выход'}

dict_print(data)
start_nun = input('Введите пункт меню > ')
print()
menu(start_nun)
