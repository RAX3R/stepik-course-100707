n = int(input())

mask = (1 << 3) | (1 << 6)

print("ДА" if n & mask == mask else "НЕТ")
