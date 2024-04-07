def get_data_fig(*args, **kwargs):
    t = ('type', 'color', 'closed', 'width')
    return tuple([sum(args)] + [kwargs[i] for i in t if i in kwargs])
