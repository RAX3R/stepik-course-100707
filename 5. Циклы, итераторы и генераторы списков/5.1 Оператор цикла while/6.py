num = list(input())

s = 1

while num:
    s *= int(num.pop())

print(s)
