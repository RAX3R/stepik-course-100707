import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

g = (tuple(map(int, lst.split())) for lst in lst_in)
z = zip(*g)
result = zip(*z)

for i in result:
    print(*i)
