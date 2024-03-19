s = input().lower().split()

d = {i: s.count(i) for i in s}

print(d.get("и", 0))
