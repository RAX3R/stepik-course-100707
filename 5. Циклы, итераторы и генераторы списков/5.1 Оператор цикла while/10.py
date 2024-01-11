n, m = map(int, input().split())

lst = []

while n < m:
    lst.append(n + 1)
    n += 2
    
print(*lst)
