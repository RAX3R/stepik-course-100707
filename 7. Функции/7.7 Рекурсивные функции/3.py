N = int(input())

def fib_rec(N, f=[]):
    if len(f) < N:
        if len(f) < 2:
            f.append(1)
        else:
            f.append(f[-2] + f[-1])
        fib_rec(N, f)
    return f
