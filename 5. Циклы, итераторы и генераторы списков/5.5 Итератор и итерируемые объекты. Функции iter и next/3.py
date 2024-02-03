num = input()

it = iter(num)

for _ in range(len(num)):
    print(next(it), end=" ")
