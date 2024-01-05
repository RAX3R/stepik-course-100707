price = float(input())

n = 2
lst = []

while n <= 10:
    lst.append(round(price * n, 1))
    n += 1

print(*lst)
