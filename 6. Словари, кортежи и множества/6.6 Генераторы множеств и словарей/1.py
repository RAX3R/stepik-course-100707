s = input().split()

d = {}
key = int(s[0])

for i in s[1:]:
    d[key] = d.get(key, i)
    key += 1

print(d[4])
