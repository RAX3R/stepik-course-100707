names = tuple(input().lower().split())

print(*tuple(name for name in names if "ва" in name))
