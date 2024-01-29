s = input()

s_2 = s.replace("-", "+")
nums = list(map(int, s_2.split("+")))
result = nums[0]
del nums[0]

for i, j in enumerate(s):
    if j == "+":
        result += nums[0]
        del nums[0]
    elif j == "-":
        result -= nums[0]
        del nums[0]

print(result)
