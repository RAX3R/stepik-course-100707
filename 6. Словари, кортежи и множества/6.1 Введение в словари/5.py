s = input().split()

d = dict()

for i in s:
    d[i[:2]] = d.get(i[:2], []) + [i]

print(*sorted(d.items()))
