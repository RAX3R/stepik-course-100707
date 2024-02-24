import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict()

for i in lst_in:
    phone, name = i.split()
    d[name] = d.get(name, []) + [phone]

print(*sorted(d.items()))
