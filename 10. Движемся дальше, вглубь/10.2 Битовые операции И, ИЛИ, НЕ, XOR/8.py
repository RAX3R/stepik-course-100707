n = int(input())

mask = (1 << 1) | (1 << 5)

print("ДА" if n & mask else "НЕТ")
