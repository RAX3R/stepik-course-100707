lst = list(map(int, input().split()))

print(sum([i for i in lst if i % 2 == 1]))
