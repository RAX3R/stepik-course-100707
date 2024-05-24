cities = input().split()

print(*map(lambda x: "-" if len(x) <= 5 else x, cities))
