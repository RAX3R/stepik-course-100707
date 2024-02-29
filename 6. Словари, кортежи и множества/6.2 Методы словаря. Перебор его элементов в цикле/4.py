import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict()

for i in lst_in:
    k, v = i.split()
    d[int(k)] = d.get(int(k), []) + [v]

for key, value in d.items():
    s = ", ".join(value)
    print(f'{key}: {s}')
