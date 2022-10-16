import in_out

def search_data(id_pes):
    list_data = in_out.get_info("general_work_personnel\PI.csv.txt")  
    list_data += in_out.get_info("general_work_personnel\Salary.csv.txt")  
    list_data += in_out.get_info("general_work_personnel\Department.csv.txt")
    count = 0
    for i in list_data:
        if f"ID {id_pes}" in i:
            print(i)
            count += 1
    if count == 0:
        print("Информация не найдена")