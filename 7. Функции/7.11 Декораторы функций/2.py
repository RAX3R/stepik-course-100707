def show_menu(func):
    def wrapper(*args):
        w = func(*args)
        for i, j in enumerate(w):
            print(f'{i + 1}. {j}')
    return wrapper


@show_menu
def get_menu(s):
    return s.split()
