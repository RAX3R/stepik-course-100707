import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

print(len(set(i.split(": ")[0] for i in lst_in)))
