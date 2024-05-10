try:
    with open("abc.txt") as file:
        r = file.read(1)
except FileNotFoundError:
    print("File Not Found")
