def func_show(func):
    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')
    return wrapper


def get_sq(width, height):
    return width * height
