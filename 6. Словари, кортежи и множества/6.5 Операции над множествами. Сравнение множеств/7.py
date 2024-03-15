num = int(input())

s_1 = {1, 2, 3, 5, 7}
s_2 = {2, 3, 5}
s_3 = set()

for i in s_1:
    if num % i == 0:
        s_3.add(i)

print("ДА" if s_2.issubset(s_3) else "НЕТ")
