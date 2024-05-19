def gen_nums():
    for i in range(2, 10000):
        c = 0
        for j in range(2, i):
            if i % j == 0:
                c += 1
        if c == 0:
            yield i

g = gen_nums()

print(*(next(g) for _ in range(20)))
