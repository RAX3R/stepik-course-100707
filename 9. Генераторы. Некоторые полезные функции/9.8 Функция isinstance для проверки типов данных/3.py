def get_even_sum(it):
    return sum(filter(lambda x: (isinstance(x, int) and not isinstance(x, bool)) and x % 2 == 0, it))
