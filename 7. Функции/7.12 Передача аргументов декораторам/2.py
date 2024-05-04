def add_tag(tag="h1"):
    def function(func):
        def wrapper(*args, **kwargs):
            new_string = f'<{tag}>{func(*args, **kwargs)}</{tag}>'
            return new_string
        return wrapper
    return function


@add_tag(tag="div")
def to_lower(string):
    return string.lower()


result = to_lower(input())

print(result)
