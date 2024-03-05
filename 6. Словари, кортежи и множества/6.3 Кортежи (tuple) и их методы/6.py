nums = tuple(map(int, input().split()))

result = tuple()

for i, j in enumerate(nums):
    if nums.count(j) > 1:
        result += (i,)

print(*result)
