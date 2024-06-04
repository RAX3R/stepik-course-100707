import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))
    
d = {i: int(j) for i, j in [z.split(":") for z in lst_in]}

print(*[k for k, _ in sorted(d.items(), key=lambda x: x[1])[:3]])
