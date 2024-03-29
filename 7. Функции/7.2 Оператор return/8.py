def function(s):
    return s, len(s)

cities = input().split()

d = dict(function(city) for city in cities)

a = sorted(d, key=lambda x: d[x])

print(*a)
