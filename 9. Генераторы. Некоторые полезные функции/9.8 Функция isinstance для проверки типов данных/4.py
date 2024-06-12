def get_list_dig(lst):
    return list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), lst))
