import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {key: int(item) for key, item in (i.split('=') for i in lst_in)}

print(*sorted(d, key=d.get, reverse=True))
