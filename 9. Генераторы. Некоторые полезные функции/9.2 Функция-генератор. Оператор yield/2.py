N = int(input())


def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for i in range(max_len):
        if i < 3:
            yield 1
        else:
            yield a + b + c
            a, b, c = b, c, a + b + c

g = balak_seq(N)

print(*(next(g) for _ in range(N)))
