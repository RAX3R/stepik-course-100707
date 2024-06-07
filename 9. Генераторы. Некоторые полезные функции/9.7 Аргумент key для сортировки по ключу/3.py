notes = ("до", "ре", "ми", "фа", "соль", "ля", "си")

s = input().split()

print(*sorted(s, key=notes.index))
