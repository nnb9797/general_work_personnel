import in_out
from logger import *
import ui
from search import *
from answers import *


def button_click():
    ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию \n3. Поиск по ID")
    user_answer = ui.input_data("Введите цифру: ")
    print()
    if user_answer == "1":
        print_all()
    elif user_answer == "2":
        add_data()
    elif user_answer == "3":
        id_pes = input("Введите id: ")
        search_data(id_pes)
        info_logger(f'Запрос на поиск по ID {id_pes}')
