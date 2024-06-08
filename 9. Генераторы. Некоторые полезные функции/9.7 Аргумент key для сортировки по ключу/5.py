import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

rank = ("рядовой", "сержант", "старшина", "прапорщик", "лейтенант", "капитан", "майор", "подполковник", "полковник")
lst = [i.split('=') for i in lst_in]
lst.sort(key=lambda x: rank.index(x[1]))
