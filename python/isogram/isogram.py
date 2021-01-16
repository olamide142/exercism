def is_isogram(string: str) -> bool:

    string = string.lower()

    if not string:
        return True

    dictionary = {}

    for i in string:
        if i in dictionary and i.isalpha:
            return False
        if i.isalpha():
            dictionary[i] = 0
            
    return True