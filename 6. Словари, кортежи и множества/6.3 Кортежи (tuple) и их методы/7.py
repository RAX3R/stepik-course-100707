t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = int(input())

t_2 = tuple(t[i][:N] for i in range(N))

for s in t_2:
    print(*s)
