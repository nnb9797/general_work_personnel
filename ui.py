def print_data(text=''):
    print(f"{text}")

def input_data(text=''):
    return input(f"{text}")

def add_data():
    id = input("Введите id: ")
    surname = input("surname: ")
    name = input("name: ")
    patronymic = input("patronymic: ")
    phone = input("phone: ")
    return f"phone: +7 {phone} surname: {surname} name: {name} patronymic: {patronymic}"


def print_all(data):
    for i in data:
        print(i)