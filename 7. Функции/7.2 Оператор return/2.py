def is_triangle(a_1, b_1, c_1):
    return (a_1 + b_1 > c_1) and (a_1 + c_1 > b_1) and (b_1 + c_1 > a_1)
