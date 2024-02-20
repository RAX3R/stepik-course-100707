import sys


s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

new_lst = [[j[i] for j in lst_in] for i in range(len(lst_in[0]))]

for row in new_lst:
    print(*row)
