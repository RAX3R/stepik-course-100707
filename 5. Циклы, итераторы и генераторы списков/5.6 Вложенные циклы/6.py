nums = list(map(int, input().split()))

s = len(nums)

for i in range(s - 1):
    i_min = nums[i]
    to_change = False
    for j in range(i + 1, s):
        if i_min > nums[j]:
            i_min = nums[j]
            index = j
            to_change = True
    if to_change:
        nums[i], nums[index] = i_min, nums[i]

print(*nums)
