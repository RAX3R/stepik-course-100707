def counter_add(tag="h1"):
    def add_num(s):
        return f'<{tag}>{s}</{tag}>'
    return add_num

string = input()

result = counter_add()

print(result(string))
