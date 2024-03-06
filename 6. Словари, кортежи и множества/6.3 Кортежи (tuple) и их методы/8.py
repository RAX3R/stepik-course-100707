import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = tuple(tuple(i.split()) for i in lst_in)

print(menu)
