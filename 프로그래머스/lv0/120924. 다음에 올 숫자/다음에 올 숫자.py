def classify_seq(common):
    a, b, c = common[0], common[1], common[2]

    if(2 * b == a + c):
        return True
    return False


def solution(common):
    a, b = common[0], common[1]

    if(classify_seq(common)):
        d = b - a
        return common[-1] + d
    
    return common[-1] * (b / a)

