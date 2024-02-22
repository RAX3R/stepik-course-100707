s = input().split()

d = dict()

for i in s:
    key, item = i.split("=")
    d[key] = d.get(key, item)

print("ДА" if 'house' in d and 'True' in d and '5' in d else "НЕТ")
