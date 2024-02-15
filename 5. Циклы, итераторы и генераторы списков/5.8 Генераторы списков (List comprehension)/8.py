s_1 = input().split()
s_2 = input().split()

print(*[int(s_1[i]) + int(s_2[i]) for i in range(len(s_1))])
