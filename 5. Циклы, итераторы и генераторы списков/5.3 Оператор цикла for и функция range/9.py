cities = [i.lower().rstrip("ьъы") for i in input().split()]

result = "ДА"

for i in range(len(cities) - 1):
    if cities[i][-1] != cities[i + 1][0]:
        result = "НЕТ"
        break
    
print(result)
