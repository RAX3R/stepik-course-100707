m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

lst = m.split("\n")

s = int(input())

if s == 1:
    print(lst[0])
elif s == 2:
    print(lst[1])
elif s == 3:
    print(lst[2])
elif s == 4:
    print(lst[3])
elif s == 5:
    print(lst[4])
elif s == 6:
    print(lst[5])
