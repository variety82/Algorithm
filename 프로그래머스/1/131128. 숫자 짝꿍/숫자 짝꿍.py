from collections import Counter
def solution(X, Y):
    X = "".join(sorted(list(X)))
    Y = "".join(sorted(list(Y)))
    x = Counter(X)
    y = Counter(Y)
    answer = ''
    for key in x:
        answer += (min(x[key], y[key]) * str(key))
    if len(answer) == 0:
        answer = "-1"
    elif answer[-1] == "0":
        answer = "0"
    else:
        answer = answer[::-1]
    return answer