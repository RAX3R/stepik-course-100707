d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(dd, a=[]):
    for i in dd:
        if isinstance(i, list):
            get_line_list(i)
        else:
            a.append(i)
    return a
