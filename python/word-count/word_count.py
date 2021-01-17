import string

def check(words):
    temp = ''
    for i,j in enumerate(words.lower()):
        if j in string.ascii_letters:
            temp += j
        if j in string.digits:
            temp += j
        if j in string.whitespace:
            temp += " "
        if j in string.punctuation:
            if j == "'":
                try:
                    if (words[i-1] in string.ascii_letters) and \
                    (words[i+1] in string.ascii_letters):
                        temp += j
                except:
                    continue
            else:
                temp += ' '
    return temp  
    
    
def count_words(sentence):
    dictionary = {}

    for i in check(sentence).split(' '):   
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1        

    if '' in dictionary:
        del dictionary['']
    return dictionary

