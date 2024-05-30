import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

g = (tuple(map(int, lst.split())) for lst in lst_in)
result = zip(*g)

for i in result:
    print(*i)
