nums = list(map(int, input().split()))

if nums[0] <= nums[1] and nums[0] <= nums[2]:
    print(nums[0])
elif nums[1] <= nums[0] and nums[1] <= nums[2]:
    print(nums[1])
elif nums[2] <= nums[0] and nums[2] <= nums[1]:
    print(nums[2])
