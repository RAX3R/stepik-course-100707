lst = input().split()

print(*sorted(lst, key=len, reverse=True))
