n = int(input())

s = 1000

while n > 0:
    s *= 1.05
    n -= 1

print(round(s, 2))
