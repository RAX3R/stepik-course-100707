a, b = map(int, input().split())

g = (0.5 * pow(x / 100, 2) - 2.0 for x in range(a  * 100, (b + 1) * 100))

print(*(round(next(g), 2) for _ in range(20)))
