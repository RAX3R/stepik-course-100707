import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

result = "ДА"

for i in range(5):
    for j in range(5):
        if lst_in[i][j] != lst_in[j][i]:
            result = "НЕТ"

print(result)
