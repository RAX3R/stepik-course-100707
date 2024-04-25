def counter_add():
    def add_num(n):
        return n + 5
    return add_num

k = int(input())

cnt = counter_add()

print(cnt(k))
