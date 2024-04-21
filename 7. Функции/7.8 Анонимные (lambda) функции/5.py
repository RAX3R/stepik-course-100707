def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

nums = list(map(int, input().split()))

print(*filter_lst(nums))
print(*filter_lst(nums, lambda x: x < 0))
print(*filter_lst(nums, lambda x: x >= 0))
print(*filter_lst(nums, lambda x: 3 <= x <= 5))
