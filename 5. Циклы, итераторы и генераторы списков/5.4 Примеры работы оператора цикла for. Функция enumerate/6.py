nums = list(map(float, input().split()))

m = nums[0]

for n in nums:
    if n < m:
        m = n

print(m)
