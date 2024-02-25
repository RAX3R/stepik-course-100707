import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict()

for i in lst_in:
    if i not in d:
        d[i] = d.get(i, i)
        print("HTML-страница для адреса", d.get(i))

    else:
        print("Взято из кэша: HTML-страница для адреса", d.get(i))
