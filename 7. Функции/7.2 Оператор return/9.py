def function(a, b):
    return a * b

nums = list(map(int, input().split()))

print(function(max(nums), min(nums)))
