
from datetime import datetime

# Применить написанный логгер к приложению из любого предыдущего д/з.

def decorator(func):
    def wrapper(*args, **kwargs):
        dt = datetime.now()
        name_func = func.__name__
        res = func(*args, **kwargs)
        try:
            with open("decorator_write.txt", "w", encoding="UTF-8") as file:
                file.write(
                    f"Дата и время вызова функции - {dt},\nИмя функции - {name_func},\nАргументы функции - {args, kwargs},\nРезультат вызова - {res}")
        except:
            print("Ошибка при работе с файлом")
        return res

    return wrapper

#генератор по разбору списка разного уровня вложенности
@decorator
def get_data_list(list_list):
    for item in list_list:
        if isinstance(item, list):
            for i in get_data_list(item):
                yield i
        else:
            yield item

a = [[[1, 2], [3, 4]], [5]]

for n in get_data_list(a):
    print(n)
print(get_data_list(a))
