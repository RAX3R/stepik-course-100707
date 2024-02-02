string = input()

it = iter(string)
s = next(it)

while s != " ":
    print(s, end="")
    s = next(it)
