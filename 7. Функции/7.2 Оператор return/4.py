def function(num):
    return num % 2 == 0

n = int(input())

while n != 1:
    if function(n):
        print(n)
    n = int(input())
