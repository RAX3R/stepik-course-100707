lst = list(map(int, input().split()))

num = lst.pop()
lst.append(num % 2 != 0)

print(*lst)
