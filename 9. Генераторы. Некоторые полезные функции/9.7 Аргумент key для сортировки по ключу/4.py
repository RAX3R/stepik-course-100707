import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

order = ("Имя", "Зачет", "Оценка", "Номер")
t = tuple(tuple(int(s) if s.isdigit() else s for s in x.split(";")) for x in lst_in)
t_sorted = tuple(zip(*sorted(zip(*t), key=lambda x: order.index(x[0]))))
