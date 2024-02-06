n = int(input())

lst = []

for i in range(2, n):
    c = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            c += 1
    if c == 0:
        lst.append(i)

print(*lst)
