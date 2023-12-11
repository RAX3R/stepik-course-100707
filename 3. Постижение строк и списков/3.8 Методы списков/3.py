num = input()

lst = list(num)
del lst[0]
lst[0] = "8"
lst.remove("-")
lst.remove("-")

print("".join(lst))
