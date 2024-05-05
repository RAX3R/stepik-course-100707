t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replace_chars(chars="!?"):
    def function(func):
        def wrapper(*args):
            result = func(*args)
            for i in result:
                if i in chars:
                    result = result.replace(i, "-")
            while "--" in result:
                result = result.replace("--", "-")
            return result
        return wrapper
    return function


@replace_chars(chars="?!:;,. ")
def to_en(st):
    new_st = ""
    for i in st.lower():
        if i in t:
            new_st += t.get(i)
        else:
            new_st += i
    return new_st


s = input()

print(to_en(s))
