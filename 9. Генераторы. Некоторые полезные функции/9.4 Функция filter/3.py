nums = map(int, input().split())

print(*filter(lambda x: 10 <= abs(x) <= 99, nums))
