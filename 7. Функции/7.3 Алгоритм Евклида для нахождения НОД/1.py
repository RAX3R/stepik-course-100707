def get_nod(a_1, b_1):
    while a_1 != b_1:
        if a_1 > b_1:
            a_1 -= b_1
        else:
            b_1 -= a_1
    return a_1
