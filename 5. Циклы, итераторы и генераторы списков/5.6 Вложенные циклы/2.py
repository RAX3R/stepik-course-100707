import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

for s in lst_in:
    while "  " in s:
        s = s.replace("  ", " ")
    s = list(s)
    for i, j in enumerate(s):
        if j == " ":
            s[i] = "-"
    print("".join(s))
