def function(string, tag="h1"):
    return f'<{tag}>{string}</{tag}>'

s = input()

print(function(s))
print(function(s, "div"))
