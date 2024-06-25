import sys
import random


random.seed(1)

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [list(map(int, x.split())) for x in lst_in]
z = list(zip(*lst))
random.shuffle(z)

for i in zip(*z):
    print(*i)
