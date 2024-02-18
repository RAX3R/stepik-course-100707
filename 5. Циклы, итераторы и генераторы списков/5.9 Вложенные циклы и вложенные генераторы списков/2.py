nums = list(map(int, input().split()))

n = int(len(nums) ** 0.5)

print([[nums[i * n + j] for j in range(n)] for i in range(n)])
