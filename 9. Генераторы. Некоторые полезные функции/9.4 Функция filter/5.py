alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@."

def function(mail):
    if ("@" in mail) and ("." in mail) and (mail.find(".") > mail.find("@") + 1):
        for i in mail:
            if i not in alphabet:
                return False
    else:
        return False
    return True

mails = input().split()

print(*filter(function, mails))
