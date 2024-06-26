import random


random.seed(1)

N = int(input())
P = [[0] * N for i in range(N)]
P_2 = [[0] * (N + 1) for i in range(N + 1)]
M = 10

def check(lst, r, c):
    return sum([lst[r][c], lst[r + 1][c + 1], lst[r - 1][c - 1], lst[r + 1][c], lst[r - 1][c], lst[r][c + 1], lst[r][c - 1], lst[r + 1][c - 1], lst[r - 1][c + 1]]) == 0

def check_row(r):
    return sum(r) == 0

for i in range(N):
    j = random.randint(0, N - 1)
    while check_row(P[i]):
        if check(P_2, i, j):
            P[i][j] = 1
            P_2[i][j] = 1
        else:
            j = random.randint(0, N - 1)

M -= N

while M != 0:
    row = random.randint(0, N - 1)
    col = random.randint(0, N - 1)
    if check(P_2, row, col):
        P[row][col] = 1
        P_2[row][col] = 1
        M -= 1
