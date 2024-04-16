n = int(input())

def fact_rec(num):
    if num == 1:
        return num
    elif num == 0:
        return 1
    return num * fact_rec(num - 1)
