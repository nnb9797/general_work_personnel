from in_out import *
from logger import *
from ui import *

def print_all():
    list_data = get_info("general_work_personnel\PI.csv.txt")  
    list_data += get_info("general_work_personnel\Salary.csv.txt")  
    list_data += get_info("general_work_personnel\Department.csv.txt")  
    for i in list_data:
        print(i)    
    info_logger(f'Запрос на вывод информации')

def add_data():
    id_pes = input_data("Введите id: ")

    data_personal = add_data_pi(id_pes)
    append_data("general_work_personnel\PI.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "PI" {data_personal}')

    data_personal = add_data_Salary(id_pes)
    append_data("general_work_personnel\Salary.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "Salary" {data_personal}')

    data_personal = add_data_Department(id_pes)
    append_data("general_work_personnel\Department.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "Department" {data_personal}')

    print_data("\nДанные успешно добавлены.")