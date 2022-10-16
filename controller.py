import in_out
import logger
import ui

def button_click():
    ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию")
    user_answer = ui.input_data()
    if user_answer == "1":
        list_data = in_out.get_info("general_work_personnel\PI.csv.txt")  
        # list_data += in_out.get_info("general_work_personnel\Salary.csv")  
        #list_data += in_out.get_info("name_file")  # дописать 
        ui.print_all(list_data)
        logger.info_logger(f'Запрос на вывод информации')
    elif user_answer == 2:
        data_personal = UI.add_data()
        in_out.append("PI.csv", data_personal)  

button_click()