import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

t = tuple(map(lambda x: tuple(x.split("=")), lst_in))
f = filter(lambda x: int(x[1]) > 500, t)
g = (i for i, j in f)

print(*g)
