import in_out
import logger
import ui
import search

def button_click():
    ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию \n3. Поиск по ID")
    user_answer = ui.input_data("Введите цифру: ")
    print()
    if user_answer == "1":
        ui.print_all()
    elif user_answer == "2":
        id_pes = ui.input_data("Введите id: ")

        data_personal = ui.add_data_pi(id_pes)
        in_out.append_data("general_work_personnel\PI.csv.txt", data_personal)
        logger.info_logger(f'Новая запись в таблицу "PI" {data_personal}')

        data_personal = ui.add_data_Salary(id_pes)
        in_out.append_data("general_work_personnel\Salary.csv.txt", data_personal)
        logger.info_logger(f'Новая запись в таблицу "Salary" {data_personal}')

        data_personal = ui.add_data_Department(id_pes)
        in_out.append_data("general_work_personnel\Department.csv.txt", data_personal)
        logger.info_logger(f'Новая запись в таблицу "Department" {data_personal}')

        ui.print_data("\nДанные успешно добавлены.")
        
    elif user_answer == "3":
        id_pes = input("Введите id: ")
        search.search_data(id_pes)
        logger.info_logger(f'Запрос на поиск по ID {id_pes}')
