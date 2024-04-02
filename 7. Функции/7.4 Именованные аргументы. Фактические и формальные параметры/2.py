def check_password(s, chars="$%!?@#"):
    if len(s) >= 8:
        return bool(set(s) & set(chars))
    return False
