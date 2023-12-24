num = input()

lst = list(map(int, num))

print("ДА" if sum(lst[:3]) == sum(lst[3:]) else "НЕТ")
