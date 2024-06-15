import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

pole = [i.split() for i in lst_in]

def is_free(lst):
    return any(any(x == "#" for x in s) for s in lst)
