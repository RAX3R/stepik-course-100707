s = input().split()

def function(city):
    return len(city) >= 6

lst = [i for i in s if function(i)]

print(*lst)
