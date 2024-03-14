s_1 = set(map(int, input().split()))

s_2 = {2}

print("НЕ ДОПУЩЕН" if s_2.issubset(s_1) else "ДОПУЩЕН")
