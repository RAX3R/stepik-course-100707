nums_1 = list(map(int, input().split()))
nums_2 = list(map(int, input().split()))

nums_1.sort()
nums_2.sort(reverse=True)

print(*map(sum, zip(nums_1, nums_2)))
