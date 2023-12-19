word = input().lower()

print("ДА" if word == word[::-1] else "НЕТ")
