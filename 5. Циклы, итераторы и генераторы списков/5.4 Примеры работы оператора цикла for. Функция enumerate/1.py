s = input()

lst = []

if "ра" in s:
    for i, j in enumerate(s):
        if j == "а" and s[i - 1] == "р":
            lst.append(i - 1)
    print(*lst)
else:
    print(-1)
