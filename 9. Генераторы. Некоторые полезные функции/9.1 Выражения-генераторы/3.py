a, b = map(int, input().split())

nums = (abs(x) for x in range(a, b + 1))

for i in range(5):
    print(next(nums))
