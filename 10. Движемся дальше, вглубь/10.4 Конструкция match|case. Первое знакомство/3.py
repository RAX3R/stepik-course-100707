def get_data(value):
    match value:
        case int() as command if command > 0:
            return value
        case float() as command if -100 <= command <= 100:
            return value
        case str():
            return value
    return None
