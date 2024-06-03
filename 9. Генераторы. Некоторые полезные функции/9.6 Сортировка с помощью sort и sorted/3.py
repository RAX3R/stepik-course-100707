nums = set(map(int, input().split()))

result = sorted(nums, reverse=True)

print(*result[:4])
