
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