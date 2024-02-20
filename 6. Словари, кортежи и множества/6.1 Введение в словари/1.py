s = input().split()

d = dict()

for i in s:
    key, item = i.split("=")
    d[key] = d.get(key, int(item))

print(*sorted(d.items()))
