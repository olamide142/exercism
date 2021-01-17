import string

def is_pangram(sentence: str)-> bool:
    for i in string.ascii_lowercase:
        if i not in sentence.lower():
            return False
    return True