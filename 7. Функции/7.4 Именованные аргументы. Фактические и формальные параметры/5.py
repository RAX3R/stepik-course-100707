def function(string, tag="h1", up=True):
    if up:
        tag = tag.upper()
    else:
        tag = tag.lower()
    return f'<{tag}>{string}</{tag}>'

s = input()

print(function(s, "div"))
print(function(s, "div", False))
