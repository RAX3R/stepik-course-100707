nums = list(map(float, input().split()))

for i, j in enumerate(nums):
    if j < 0:
        nums[i] = -1.0

print(*nums)
