num = int(input())

d = dict()

while num != 0:
    if num not in d:
        d[num] = d.get(num, round(num ** 0.5, 2))
        print(d.get(num))

    else:
        print("значение из кэша:", d.get(num))
    num = int(input())
