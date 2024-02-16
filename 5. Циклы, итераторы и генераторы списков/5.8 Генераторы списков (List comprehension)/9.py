s = input().split()

lst = [[s[i], int(s[i + 1])] for i, j in enumerate(s) if j.isalpha()]

print(lst)
