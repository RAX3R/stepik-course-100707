def s(func):
    def wrapper(*args, **kwargs):
        start = 5
        nums = func(*args, **kwargs)
        return start + sum(nums)
    return wrapper


@s
def to_list(lst):
    return [int(i) for i in lst.split()]


result = to_list(input())

print(result)
