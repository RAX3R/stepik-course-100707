m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

n1, n2, n3 = map(int, input().split())

m1 = "#" + m[n1 - 1] if n1 in [1, 4] else m[n1 - 1]
m2 = "#" + m[n2 - 1] if n2 in [1, 4] else m[n2 - 1]
m3 = "#" + m[n3 - 1] if n3 in [1, 4] else m[n3 - 1]

print(m1, m2, m3)
