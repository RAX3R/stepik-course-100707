import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict()

for i in lst_in:
    key, item = i.split("=")
    d[int(key)] = d.get(int(key), item)

print(*sorted(d.items()))
