import sys


s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

print(*[j for i in lst_in[::-1] for j in i[::-1]])
