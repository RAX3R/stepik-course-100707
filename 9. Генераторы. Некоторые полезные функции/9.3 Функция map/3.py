import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = [list(map(int, i.split())) for i in lst_in]
