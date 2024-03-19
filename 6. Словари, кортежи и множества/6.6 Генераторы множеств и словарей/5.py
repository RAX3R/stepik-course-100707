import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

new_lst = [i.split(": ") for i in lst_in]
d = {i[0]: {j[1] for j in new_lst if i[0] == j[0]} for i in new_lst}
