import random


random.seed(1)

names = input().split()

print(*random.sample(names, 3))
