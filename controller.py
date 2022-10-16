import in_out
import logger
import ui

def button_click():
    user_answer = ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию")
    if user_answer == 1:
        list_data = in_out.get_info("name_file")  # дописать 
        list_data += in_out.get_info("name_file")  # дописать 
        list_data += in_out.get_info("name_file")  # дописать 
        print(list_data)
        logger.info_logger(f'Запрос на вывод информации')
    elif user_answer == 2:
        data_personal = UI.add_data()
        in_out.append("name_file", data_personal)  # дописать 