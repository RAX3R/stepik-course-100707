t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [_, str() as author, str() as title, float() | int() as price, int() as year]:
        print("Yes")
    case _:
        print("No")
