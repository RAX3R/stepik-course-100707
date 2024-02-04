n = int(input())

m = [[1] * n] * n

for i in range(n):
    for j in range(n):
        if j == n - 1:
            m[i][j] = 5
    print(*m[i])
