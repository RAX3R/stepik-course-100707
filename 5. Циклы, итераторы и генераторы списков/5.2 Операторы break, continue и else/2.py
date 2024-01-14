n = 1
result = 1

while n != 0:
    n = int(input())
    if n <= 0:
        continue
    result *= n

print(result)
