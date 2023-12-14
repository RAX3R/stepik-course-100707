rivers = input().split()

rivers.sort()
del rivers[0]

print(*rivers)
