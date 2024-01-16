n = int(input())

i = 1
lst = []

if n < 100:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            lst.append(i)
        i += 1
    print(*lst)
else:
    print("слишком большое значение n")
