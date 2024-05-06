from functools import wraps

def f_s(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))
    return wrapper


@f_s
def get_list(string):
    '''Функция для формирования списка целых значений'''
    return map(int, string.split())
