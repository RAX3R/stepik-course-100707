s = input()
s_lst = s.split()

tp = tuple(map(tuple, [_.split('=') for _ in s_lst]))
