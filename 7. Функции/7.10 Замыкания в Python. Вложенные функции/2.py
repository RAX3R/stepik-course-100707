def counter_add(n):
    def add_num(m):
        return n + m
    return add_num

k = int(input())

cnt = counter_add(2)

print(cnt(k))
