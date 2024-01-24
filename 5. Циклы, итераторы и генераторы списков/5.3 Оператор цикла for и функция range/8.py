n = int(input())

result = "ДА"

for i in range(2, n):
    if n % i == 0:
        result = "НЕТ"
        break

print(result)
