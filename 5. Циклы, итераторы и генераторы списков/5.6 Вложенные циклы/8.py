n = int(input())

banknotes = [64, 32, 16, 8, 4, 2, 1]
lst = []
s = 0

for i in banknotes:
    while s + i <= n:
        s += i
        lst.append(i)

print(*lst)
