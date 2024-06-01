s = input()

lst = list(map(int, s.split()))
lst.sort()

tp_lst = tuple(sorted(tuple(map(int, s.split()))))
