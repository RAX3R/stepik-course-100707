def str_min(*args):
    return min(args)


def str_min3(*args):
    return str_min(args[0], str_min(*args[1:]))


def str_min4(*args):
    return str_min(args[0], str_min3(*args[1:]))
