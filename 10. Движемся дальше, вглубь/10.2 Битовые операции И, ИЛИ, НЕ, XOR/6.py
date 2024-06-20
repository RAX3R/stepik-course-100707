c = input()

key = 123

print(*map(lambda x: chr(ord(x) ^ key), c), sep="")
