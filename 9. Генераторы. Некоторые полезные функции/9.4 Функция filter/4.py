n_1 = set(map(int, input().split()))
n_2 = set(map(int, input().split()))

print(*sorted(filter(lambda x: x % 2 == 0, n_1 & n_2)))
