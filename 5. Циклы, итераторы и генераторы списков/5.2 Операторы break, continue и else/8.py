import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

i = 0

while i < len(lst_in):
    if " " in lst_in[i]:
        lst_in.pop(i)
    else:
        i += 1

print(*lst_in)
