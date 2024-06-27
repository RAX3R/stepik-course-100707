def get_data(value):
    match value:
        case int() | float() | str():
            return value
    return None
