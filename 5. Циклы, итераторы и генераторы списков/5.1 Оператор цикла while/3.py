n = int(input())

result = 0

while n > 0:
    result += 1 / n
    n -= 1

print(round(result, 3))
