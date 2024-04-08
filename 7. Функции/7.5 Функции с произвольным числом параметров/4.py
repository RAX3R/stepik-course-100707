def verify(*args):
    lst_in = args[0]
    for i in range(len(lst_in) - 1):
        for j in range(len(lst_in) - 1):
            if is_isolate(lst_in[i][j], lst_in[i][j + 1], lst_in[i + 1][j], lst_in[i + 1][j + 1]):
                return False
    return True


def is_isolate(*args):
    return sum(args) > 1
