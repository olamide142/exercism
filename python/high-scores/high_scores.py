
def latest(scores):
    return scores[-1]


def personal_best(scores):
    if len(scores) == 1:
        return scores[0]

    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    
    if len(scores) < 3:
        scores.reverse()
        return scores

    n = scores[len(scores)-3:]
    n.reverse()
    return n


print(latest([1,90,3,5,78,6,4,3]))
print(personal_best([13,53,35,45,65,76.88,34,14]))
print(personal_top_three([13,53,35,45,65,76.88,34,14]))