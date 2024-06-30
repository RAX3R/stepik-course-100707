t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [_, str() as author, str() as title] if len(author) >= 6 and len(title) >= 10:
        print("Yes")
    case [_, str() as author, str(), str() as title, float() | int() as price] if len(author) >= 6 and price > 0:
        print("Yes")
    case [_, str() as author, str() as title, int() as year] if year >= 2020:
        print("Yes")
    case [_, str() as author, str() as title, float() | int() as price, int() as year] if price > 0 and year >= 2020:
        print("Yes")
    case _:
        print("No")
