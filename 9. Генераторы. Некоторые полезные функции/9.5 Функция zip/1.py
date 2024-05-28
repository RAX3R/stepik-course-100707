n_1 = input().split()
n_2 = input().split()

result = map(lambda x: int(x[0]) * int(x[1]), zip(n_1, n_2))
 
print(*(next(result) for _ in range(3)))
