cities = input().split()

result = "ДА"

while cities:
    if len(cities.pop()) < 5:
        result = "НЕТ"
        break

print(result)
