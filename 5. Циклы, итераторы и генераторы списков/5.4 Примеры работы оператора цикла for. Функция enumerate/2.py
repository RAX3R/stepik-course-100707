num = input()

result = "ДА"

if len(num) == 16 and num.startswith("+7") and num[3:5].isdigit() and num[7:9].isdigit() and num[11:12].isdigit() and num[14:15].isdigit():
    for i, j in enumerate(num):
        if (i == 2 and j != "(") or (i == 6 and j != ")") or (i in [10, 13] and j != "-"):
            result = "НЕТ"
            break
else:
    result = "НЕТ"
        
print(result)
