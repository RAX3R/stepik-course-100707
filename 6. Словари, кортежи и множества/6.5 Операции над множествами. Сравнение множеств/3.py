s_1 = set(map(int, input().split()))
s_2 = set(map(int, input().split()))

print(*sorted(s_1 ^ s_2))
