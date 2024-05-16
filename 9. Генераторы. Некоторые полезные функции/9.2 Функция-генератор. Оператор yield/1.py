N = int(input())

def get_sum(total):
    s = 0
    for i in range(1, total + 1):
        s += i
        yield s
