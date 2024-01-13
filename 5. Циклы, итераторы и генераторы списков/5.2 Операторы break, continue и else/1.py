p = [0] * 10

while p.count(1) != 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1

print(*p)
