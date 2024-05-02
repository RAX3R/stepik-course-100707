def to_dict(func):
    def wrapper(*args, **kwargs):
        d = {}
        l_1, l_2 = func(*args, **kwargs)
        for i, j in enumerate(l_1):
            d[j] = d.get(j, l_2[i])
        return d
    return wrapper


@to_dict
def to_list(*args):
    return [i.split() for i in args]


dd = to_list(input(), input())

print(*sorted(dd.items()))
