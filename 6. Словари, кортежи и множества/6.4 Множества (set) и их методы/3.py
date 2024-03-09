s = input()

nums = sorted(set(int(i) for i in s if i.isdigit()))

if nums:
    print(*nums)
else:
    print("НЕТ")
