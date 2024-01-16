names = input().split()

result = "НЕТ"

while names:
    name = names.pop().lower()
    if name[0] == name[-1]:
        result = "ДА"
        break

print(result)
