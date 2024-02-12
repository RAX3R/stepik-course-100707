N = int(input())

matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

for s in matrix:
    print(*s)
