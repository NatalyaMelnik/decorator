#Написать декоратор из п.1, но с параметром – путь к логам.
import requests
from datetime import datetime

PATH = "decorator_write.txt"
def path_log(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dt = datetime.now()
            name_func = func.__name__
            res = func(*args, **kwargs)
            try:
                with open(path, "w", encoding="UTF-8") as file:
                    file.write(
                        f"Дата и время вызова функции - {dt},\nИмя функции - {name_func},\nАргументы функции - {args, kwargs},\nРезультат вызова - {res}")
            except:
                print("Ошибка при работе с файлом")
            return res

        return wrapper
    return decorator


@path_log(PATH)
def get_request(people_id):
    response = requests.get(f'https://swapi.dev/api/people/{people_id}').json()
    return response


print(get_request(people_id=1))