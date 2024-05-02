t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def remove_h(func):
    def wrapper(*args):
        result = func(*args)
        while "--" in result:
            result = result.replace("--", "-")
        return result
    return wrapper


@remove_h
def to_en(st, sep="-"):
    new_st = ""
    for i in st.lower():
        if i in t:
            new_st += t.get(i)
        elif i in ": ;.,_":
            new_st += sep
        else:
            new_st += i
    return new_st


s = input()

print(to_en(s))
