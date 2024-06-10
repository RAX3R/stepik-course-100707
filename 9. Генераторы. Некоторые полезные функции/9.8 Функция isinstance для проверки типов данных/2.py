def get_sum(it):
    return sum(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), it))
