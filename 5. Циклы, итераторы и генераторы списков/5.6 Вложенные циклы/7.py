nums = list(map(int, input().split()))

s = len(nums)

for i in range(s):
    for j in range(i, s):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(*nums)
