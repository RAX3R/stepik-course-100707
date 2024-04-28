def counter_add(t="h1"):
    def add_num(s):
        return f'<{t}>{s}</{t}>'
    return add_num

tag = input()
string = input()

result = counter_add(tag)

print(result(string))
