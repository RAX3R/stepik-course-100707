n = int(input())

g_1 = (x for x in range(-n, n + 1))
g_2 = (abs(x) ** 3 for x in g_1)

print(*(next(g_2) for _ in range(4)))
