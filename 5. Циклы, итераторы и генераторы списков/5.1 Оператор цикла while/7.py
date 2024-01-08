n = int(input())

lst = [1, 1]

while len(lst) < n:
    lst.append(lst[-1] + lst[-2])

print(*lst)
