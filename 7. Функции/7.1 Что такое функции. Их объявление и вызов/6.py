alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@."

def function(mail):
    if ("@" in mail) and ("." in mail):
        for i in mail:
            if i not in alphabet:
                return "НЕТ"
    else:
        return "НЕТ"
    return "ДА"

print(function(input()))
