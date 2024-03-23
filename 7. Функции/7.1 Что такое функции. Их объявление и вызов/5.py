def function(width, height):
    x = (width + height) * 2
    return f"Периметр прямоугольника, равен {x}"

w, h = map(int, input().split())

print(function(w, h))
