def show_func(func):
    def wrapper(*args):
        return sorted(func(*args))
    return wrapper


@show_func
def get_list(nums):
    return list(map(int, nums.split()))


lst = get_list(input())

print(*lst)
