def get_add(a, b):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        if isinstance(a, bool) or isinstance(b, bool):
            return None
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    return None
