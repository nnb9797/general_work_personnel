import ui
from answers import *
from logger import *


def button_click():
    info_logger(f'Справочник запущен')
    while True:
        ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию \n3. Поиск по ID \n4. Закрыть программу")
        user_answer = ui.input_data("Введите цифру: ")
        print()
        if user_answer == "1":
            print_all()
        elif user_answer == "2":
            add_data()
        elif user_answer == "3":
            search_data()
        elif user_answer == "4":
            print("Справочник закрыт")
            info_logger(f'Справочник закрыт')
            break