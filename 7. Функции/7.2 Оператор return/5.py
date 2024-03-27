def function(num):
    return int(num) % 2 == 1

lst = [int(i) for i in input().split() if function(i)]

print(*lst)
