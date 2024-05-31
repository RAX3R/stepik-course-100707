cities = input().split()

result = zip(*[iter(cities)] * 3)

for i in result:
    print(*i)
