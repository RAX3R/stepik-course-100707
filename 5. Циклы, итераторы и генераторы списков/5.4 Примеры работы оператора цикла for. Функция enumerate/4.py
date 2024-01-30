nums = list(map(int, input().split()))

new_nums = []

for _, j in enumerate(nums):
    new_nums.append(j ** 2)

print(*new_nums)
