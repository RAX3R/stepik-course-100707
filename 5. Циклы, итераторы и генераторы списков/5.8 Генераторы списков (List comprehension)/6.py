n = int(input())

matrix = [[i for j in range(n)] for i in range(n)]

for line in matrix:
    print(*line)
