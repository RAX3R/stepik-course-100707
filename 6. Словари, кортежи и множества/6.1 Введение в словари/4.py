s = input().split()

d = dict(i.split("=") for i in s)
d.pop('False', None)
d.pop('3', None)

print(*sorted(d.items()))
