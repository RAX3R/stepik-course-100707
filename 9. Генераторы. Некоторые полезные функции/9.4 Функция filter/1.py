cities = input().split()

result = filter(lambda x: len(x) > 5, cities)

print(*(next(result) for _ in range(3)))
