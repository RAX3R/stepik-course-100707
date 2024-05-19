import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
random.seed(1)

N = int(input())


def gen_rand(ln):
    yield ''.join([chars[random.randint(0, len(chars) - 1)] for _ in range(ln)])

for _ in range(5):
    print(next(gen_rand(N)))
