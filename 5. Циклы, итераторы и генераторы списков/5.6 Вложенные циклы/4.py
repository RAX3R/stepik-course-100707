import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

result = "ДА"

for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] > 1:
            result = "НЕТ"

print(result)
