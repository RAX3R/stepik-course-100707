nums = map(float, input().split())

print(*(next(nums) for _ in range(3)))
