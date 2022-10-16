from datetime import datetime as dt


def info_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Log.txt', 'a') as file:
        file.write(f'{time}: Info: {data}\n')


