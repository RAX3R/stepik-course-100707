nums = tuple(map(int, input().split()))

new_nums = tuple()

for i in nums:
    if i not in new_nums:
        new_nums += (i,)

print(*new_nums)
